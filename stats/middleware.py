# coding: utf-8

import sys
sys.path.append('..')


def create(obj):
    object = obj()
    object.get_stats()
