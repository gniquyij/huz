# coding: utf-8

from subprocess import run
import sys
sys.path.append('..')
import settings


# hzell: huz + shell


def bash_run(cmd):
    session = run(cmd, shell=True, capture_output=True)
    return session.stdout


def locate_sources(src_path=settings.HUZ_SRC_PATH):
    sources = bash_run('ls %s' % src_path).decode('utf-8').split('\n')
    return sources[:-1]
