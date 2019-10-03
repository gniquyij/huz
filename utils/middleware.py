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
    if table_name != 'Release':
        title = obj.__dict__['title']
        try:
            data = hzopg.read_data(table_name, 'title', 'title', title)
            if title == data:
                return hzopg.read_data(table_name, 'id', 'title', data), metainfo
        except TypeError:   # TODO: when init, no data then "TypeError: 'NoneType' object is not subscriptable"
            pass
    return hzopg.insert_data('%s' % table_name, col_names[:-2], '(%s)' % col_values[:-2]), metainfo
