# coding: utf-8

import sys
sys.path.append('..')
from prepost.pre import create_table_in_db
import utils.middleware


@create_table_in_db
class Track:
    def __init__(self):
        # self.genre = str
        self.release_id = int
        self.title = str

    def get_release_info(self, release_id):
        self.release_id = release_id

    def get_metainfo(self, metainfo):
        # self.genre = utils.middleware.get_kvalue_from_json(metainfo['format']['tags'], 'genre')
        self.title = utils.middleware.get_kvalue_from_json(metainfo['format']['tags'], 'title')
