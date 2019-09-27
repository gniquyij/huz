# coding: utf-8

import sys
sys.path.append('')
from utils import hzopg, middleware
from release.models import Release


def create(file_path, obj=Release):
    object = obj()
    return middleware.create(file_path, object)


def update(id, field_name, field_value):
    return hzopg.update_data('release', field_name, field_value, 'id', id)
