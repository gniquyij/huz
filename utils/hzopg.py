# coding: utf-8

import psycopg2
import settings
import sys
sys.path.append('..')
from utils import hzell


# hzopg: huz + psycopg


def connect(cmd=settings.HUZ_PSQL_CONNECT_CMD):
    return psycopg2.connect(cmd)


def create_table(table_name, headers):
    import datetime
    for k, v in headers.items():
        if v is str:
            headers[k] = 'text'
        elif v is int:
            headers[k] = 'integer'
        elif v == datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
            headers[k] = 'timestamp'
    statement = ''
    for k, v in headers.items():
        piece = k + ' ' + v + ', '
        statement += piece

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("select exists (select * from information_schema.tables where table_schema = 'public' and table_name = '%s');" % table_name.lower())
    resp = cursor.fetchone()
    if not resp[0]:
        cursor.execute('create table %s (%s);' % (table_name.lower(), statement[:-2]))
        create_primary_key(cursor, table_name.lower())
        conn.commit()


def create_primary_key(cursor, table_name):
    cursor.execute("alter table %s add column id serial primary key;" % table_name)


def insert_data(table_name, col_names, col_values):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("insert into %s (%s) values %s returning id;" % (table_name, col_names, col_values))
    resp = cursor.fetchone()
    conn.commit()
    return resp[0]


def update_data(table_name, col_name, col_value, benchmark_col_name, benchmark_col_value):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("update %s set %s = %s where %s = %s;" % (table_name, col_name, col_value, benchmark_col_name, benchmark_col_value))
    conn.commit()


def dump_data_in_json(col_names, table_name, file_path):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('copy (select json_agg(t) from (select %s from %s) t) to %s;' % (col_names, table_name, file_path))
    conn.commit()
    hzell.bash_run("echo $(cat %s | tr -d '\\n') > %s" % (file_path, file_path))
