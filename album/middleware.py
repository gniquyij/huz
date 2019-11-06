# coding: utf-8

import sys
sys.path.append('')
from utils import hzopg, middleware
from album.models import Album


def create_album(metainfo, release_id, obj=Album):
    object = obj()
    object.get_release_info(release_id)
    return middleware.create(metainfo, object)


def update_album(id, field_name, field_value):
    return hzopg.update_data('album', field_name, field_value, id, 'any(release_ids)')
