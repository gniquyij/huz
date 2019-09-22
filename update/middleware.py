# coding: utf-8

import sys
sys.path.append('')
from utils import hzopg


def create(release_id, action, updated_at):
    update = {
        'release_id': release_id,
        'action': action,
        'updated_at': updated_at,
    }
    col_names = ''
    for key in update.keys():
        col_names += '%s, ' % key
    col_values = ''
    for value in update.values():
        col_values += "'%s', " % value
    hzopg.insert_data('update', col_names[:-2], '(%s)' % col_values[:-2])
