# coding: utf-8

import sys
sys.path.append('..')
from prepost.pre import create_table_in_db


@create_table_in_db
class Track:
    def __init__(self):
        self.genre = str
        self.release_id = int
        self.title = str

    def get_release_info(self, release_id):
        self.release_id = release_id

    def get_metainfo(self, metainfo):
        self.genre = ''
        if 'genre' in metainfo['format']['tags']:
            self.genre = metainfo['format']['tags']['genre']
        self.title = metainfo['format']['tags']['title']
