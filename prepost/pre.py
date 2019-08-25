# coding: utf-8

import sys
sys.path.append('..')
import settings
from utils import huzell, huzopg


def create_table_in_db(cls):
    cls_name = cls.__name__
    c = cls()
    attributes = c.__dict__
    huzopg.create_table(cls_name, attributes)
    return cls


def locate_sources(src_path=settings.HUZ_SRC_PATH):
    return huzell.bash_run('ls %s' % src_path).decode('utf-8').split()


def store_src_info(src_path):
    from track.models import Track
    import track.middleware
    track.middleware.create(Track, src_path)


def main():
    models = huzell.bash_run('find %s -name "models.py"' % settings.HUZ_HOME_PATH).decode('utf-8').split()
    for model in models:
        huzell.bash_run('python %s' % model)
    sources = locate_sources()
    for src in sources:
        store_src_info(settings.HUZ_SRC_PATH + '/' + src)


if __name__ == '__main__':
    main()
