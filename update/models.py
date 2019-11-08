# coding: utf-8

from datetime import datetime
import sys
sys.path.append('..')
from bin.init import create_table_in_db


@create_table_in_db
class Update:
    def __init__(self):
        self.release_id = int
        self.action = str
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

