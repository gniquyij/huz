# coding: utf-8

from utils import hzopg


def get_cls_info(cls):
    cls_name = cls.__class__.__name__
    attr_names = ''
    for key in cls.__dict__.keys():
        attr_names += '%s, ' % key
    attr_values = ''
    for value in cls.__dict__.values():
        if value is int:
            value = 0
        if type(value) is str:
            value = value.replace("'", '')
        attr_values += "'%s', " % value
    return cls_name, attr_names, attr_values


def get_kvalue_from_json(json, kname):
    if kname in json:
        return json[kname]
    return ''


def create(file_path, obj):
    metainfo = obj.get_metainfo(file_path)
    table_name, col_names, col_values = get_cls_info(obj)
    if table_name != 'Release':
        title = obj.__dict__['title']
        title = title.replace("'", '')
        try:
            data = hzopg.read_data(table_name, 'title', 'title', title)
            if title == data:
                return hzopg.read_data(table_name, 'id', 'title', data), metainfo
        except TypeError:   # TODO: when init, no data then "TypeError: 'NoneType' object is not subscriptable"
            pass
    return hzopg.insert_data('%s' % table_name, col_names[:-2], '(%s)' % col_values[:-2]), metainfo
