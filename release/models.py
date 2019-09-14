# coding: utf-8

from datetime import datetime
import os
import sys
sys.path.append('..')
from utils import hzobe
from prepost.pre import create_table_in_db


@create_table_in_db
class Release:
    def __init__(self):
        self.track_id = int
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.accessed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.modified_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_metainfo(self, file_path):
        self.accessed_at = datetime.fromtimestamp(os.stat(file_path).st_atime).strftime("%Y-%m-%d %H:%M:%S")
        self.modified_at = datetime.fromtimestamp(os.stat(file_path).st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        self.changed_at = datetime.fromtimestamp(os.stat(file_path).st_ctime).strftime("%Y-%m-%d %H:%M:%S")
        return hzobe.get_metainfo(file_path)
