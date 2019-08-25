# coding: utf-8

from subprocess import run


# huzell: huz + shell


def bash_run(cmd):
    session = run(cmd, shell=True, capture_output=True)
    return session.stdout
