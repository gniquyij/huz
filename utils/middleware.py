# coding: utf-8

from . import hzopg


def create(file_path, obj):
    metainfo = obj.get_metainfo(file_path)
    table_name = obj.__class__.__name__
    col_names = ''
    for key in obj.__dict__.keys():
        col_names += '%s, ' % key
    col_values = ''
    for value in obj.__dict__.values():
        if value is int:
            value = 0
        col_values += "'%s', " % value
    return hzopg.insert_data('%s' % table_name, col_names[:-2], '(%s)' % col_values[:-2]), metainfo
