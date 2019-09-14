# coding: utf-8

import sys
sys.path.append('')
from utils import middleware
from release.models import Release


def create(file_path, obj=Release):
    object = obj()
    return middleware.create(file_path, object)
