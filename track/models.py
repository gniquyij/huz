# coding: utf-8

import sys
sys.path.append('..')
from utils import huzobe
from prepost.pre import create_table_in_db


@create_table_in_db
class Track:
    def __init__(self):
        self.title = str
        # self.album_id = int
        # self.artist_id = int
        import datetime
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_metainfo(self, file_path):
        metainfo = huzobe.get_metainfo(file_path)
        self.title = metainfo['format']['tags']['title']
