# coding: utf-8

import sys
sys.path.append('')
from utils import middleware
from track.models import Track


def create(metainfo, release_id, obj=Track):
    object = obj()
    object.get_release_info(release_id)
    return middleware.create(metainfo, object)
