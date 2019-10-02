# coding: utf-8

import sys
sys.path.append('')
from utils import middleware
from album.models import Album


def create(metainfo, release_id, obj=Album):
    object = obj()
    object.get_release_info(release_id)
    return middleware.create(metainfo, object)
