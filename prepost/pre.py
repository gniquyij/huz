# coding: utf-8

import sys
sys.path.append('..')
import settings
from utils import hzell, hzopg


def create_table_in_db(cls):
    cls_name = cls.__name__
    c = cls()
    attributes = c.__dict__
    hzopg.create_table(cls_name, attributes)
    return cls


def locate_sources(src_path=settings.HUZ_SRC_PATH):
    return hzell.bash_run('ls %s' % src_path).decode('utf-8').split()


def store_src_info(src_path):
    import release.middleware
    release_id, metainfo = release.middleware.create(src_path)
    import track.middleware
    track.middleware.create(metainfo, release_id)


def main():
    models = hzell.bash_run('find %s -name "models.py"' % settings.HUZ_HOME_PATH).decode('utf-8').split()
    for model in models:
        hzell.bash_run('python %s' % model)
    sources = locate_sources()
    for src in sources:
        store_src_info(settings.HUZ_SRC_PATH + '/' + src)


if __name__ == '__main__':
    main()
