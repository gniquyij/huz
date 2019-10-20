# coding: utf-8

from datetime import datetime
import sys
sys.path.append('..')
from prepost.pre import create_table_in_db
from utils import hzopg


class Stats:
    def __init__(self):
        self.count = int
        self.tag = str
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_stats(self, arg):
        obj_name = self.__class__.__name__
        self.tag = arg
        self.count = hzopg.count_data(obj_name[:-5])


@create_table_in_db
class ReleaseStats(Stats):
    pass


@create_table_in_db
class AlbumStats(Stats):
    pass


@create_table_in_db
class ArtistStats(Stats):
    pass


@create_table_in_db
class TrackStats(Stats):
    pass


@create_table_in_db
class UpdateStats(Stats):
    pass
