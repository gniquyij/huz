# coding: utf-8

import sys
sys.path.append('..')
from utils import hzopg, middleware


def create(obj, tag):
    object = obj()
    object.get_stats(tag)
    table_name, col_names, col_values = middleware.get_cls_info(object)
    hzopg.insert_data('%s' % table_name, col_names[:-2], '(%s)' % col_values[:-2])
