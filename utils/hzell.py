# coding: utf-8

from subprocess import run


# hzell: huz + shell


def bash_run(cmd):
    session = run(cmd, shell=True, capture_output=True)
    return session.stdout
