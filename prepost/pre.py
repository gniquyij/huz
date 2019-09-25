# coding: utf-8

import sys
sys.path.append('..')
import settings
from utils import hzell, hzopg, hzonitor


def create_table_in_db(cls):
    cls_name = cls.__name__
    c = cls()
    attributes = c.__dict__
    hzopg.create_table(cls_name, attributes)
    return cls


def store_src_info(src_path):
    import release.middleware
    release_id, metainfo = release.middleware.create(src_path)
    import track.middleware
    track_id = track.middleware.create(metainfo, release_id)[0]
    hzopg.update_data('release', 'track_id', track_id, 'id', release_id)


def main():
    models = hzell.bash_run('find %s -name "models.py"' % settings.HUZ_HOME_PATH).decode('utf-8').split()
    for model in models:
        hzell.bash_run('python %s' % model)
    sources = hzell.locate_sources()
    for src in sources:
        store_src_info(settings.HUZ_SRC_PATH + '/' + src)
    hzopg.dump_data_in_json('id, src_path, accessed_at, modified_at, changed_at', 'release', "'%s/dbshot.json'" % settings.HUZ_HZONITOR_TMP_PATH)
    hzonitor.update_src_stat()


if __name__ == '__main__':
    main()
