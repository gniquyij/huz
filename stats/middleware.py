# coding: utf-8

import sys
sys.path.append('..')
from utils import hzopg


def create(obj, dur):   # TODO: use create in utils/middleware?
    object = obj()
    object.get_stats(dur)
    table_name = object.__class__.__name__
    col_names = ''
    for key in object.__dict__.keys():
        col_names += '%s, ' % key
    col_values = ''
    for value in object.__dict__.values():
        if value is int:
            value = 0
        col_values += "'%s', " % value
    hzopg.insert_data('%s' % table_name, col_names[:-2], '(%s)' % col_values[:-2])
