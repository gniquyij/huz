# coding: utf-8

import sys
sys.path.append('..')
from prepost.pre import create_table_in_db


@create_table_in_db
class Track:
    def __init__(self):
        self.release_id = int
        self.title = str

    def get_release_info(self, release_id):
        self.release_id = release_id

    def get_metainfo(self, metainfo):
        self.title = metainfo['format']['tags']['title']
