# coding: utf-8

import sys
sys.path.append('')
from utils import hzopg, middleware
from artist.models import Artist


def create_artist(metainfo, release_id, obj=Artist):
    object = obj()
    object.get_release_info(release_id)
    return middleware.create(metainfo, object)


def update_artist(id, field_name, field_value):
    return hzopg.update_data('artist', field_name, field_value, id, 'any(release_ids)')
