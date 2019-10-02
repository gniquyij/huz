# coding: utf-8

import sys
sys.path.append('')
from utils import middleware
from artist.models import Artist


def create(metainfo, release_id, obj=Artist):
    object = obj()
    object.get_release_info(release_id)
    return middleware.create(metainfo, object)
