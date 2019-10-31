# coding: utf-8

import sys
sys.path.append('')
from utils import hzopg, middleware
from track.models import Track


def create_track(metainfo, release_id, obj=Track):
    object = obj()
    object.get_release_info(release_id)
    return middleware.create(metainfo, object)


def update_track(id, field_name, field_value):
    return hzopg.update_data('track', field_name, field_value, 'release_id', id)
