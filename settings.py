# coding: utf-8

import os


HUZ_HOME_PATH = os.path.dirname(os.path.realpath(__file__))
HUZ_SRC_PATH = os.path.join(HUZ_HOME_PATH, 'src')
if not os.path.isdir('%s/recorders/tmp' % HUZ_HOME_PATH):
     os.mkdir('%s/recorders/tmp' % HUZ_HOME_PATH)
HUZ_RECORDING_TMP_PATH = os.path.join(HUZ_HOME_PATH, 'recorders/tmp')


#####################
# psql database
#####################

HUZ_PSQL_DB_NAME = 'huz'
HUZ_PSQL_USER = 'huzer'
HUZ_PSQL_PASSWORD = ''
HUZ_PSQL_HOST = '<ip-address>'
HUZ_PSQL_PORT = '5432'
HUZ_PSQL_CONNECT_CMD = 'dbname=%s user=%s host=%s password=%s' % (HUZ_PSQL_DB_NAME, HUZ_PSQL_USER, HUZ_PSQL_HOST, HUZ_PSQL_PASSWORD)
