# coding: utf-8

from subprocess import run
import json


# huzobe: huz + ffprobe


def get_metainfo(filename):
    cmd = 'ffprobe -v quiet -print_format json -show_format -show_streams %s' % filename
    process = run(cmd, shell=True, capture_output=True)

    return json.loads(process.stdout)
