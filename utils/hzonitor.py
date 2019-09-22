# coding: utf-8

from datetime import datetime
import json
import os
import sys
sys.path.append('..')
import settings
from utils import hzell, hzopg
import update.middleware



def get_stat(src_path):
    accessed_at = datetime.fromtimestamp(os.stat(src_path).st_atime).strftime("%Y-%m-%dT%H:%M:%S")
    modified_at = datetime.fromtimestamp(os.stat(src_path).st_mtime).strftime("%Y-%m-%dT%H:%M:%S")
    changed_at = datetime.fromtimestamp(os.stat(src_path).st_ctime).strftime("%Y-%m-%dT%H:%M:%S")

    return accessed_at, modified_at, changed_at


def update_src_stat(path=settings.HUZ_SRC_PATH):
    settings.HUZ_SRC_STAT['accessed_at'], settings.HUZ_SRC_STAT['modified_at'], settings.HUZ_SRC_STAT['changed_at'] = get_stat(path)


def main():
    if get_stat(settings.HUZ_SRC_PATH)[0] == settings.HUZ_SRC_STAT['accessed_at'] and get_stat(settings.HUZ_SRC_PATH)[1] == settings.HUZ_SRC_STAT['modified_at'] and get_stat(settings.HUZ_SRC_PATH)[2] == settings.HUZ_SRC_STAT['changed_at']:
        return
    update_src_stat()
    sources = hzell.locate_sources()
    for src in sources:
        accessed_at, modified_at, changed_at = get_stat(settings.HUZ_SRC_PATH + '/' + src)
        with open(settings.HUZ_HOME_PATH + '/dbshot.json') as f:
            dbshot = json.load(f)
            for i in dbshot:
                last_accessed_at, last_modified_at, last_changed_at = i['accessed_at'], i['modified_at'], i['changed_at']
                if accessed_at != last_accessed_at:
                    update.middleware.create(i['id'], 'accessed', accessed_at)
                    hzopg.update_data('release', 'accessed_at', "'%s'" % accessed_at, 'id', i['id'])
                if modified_at != last_modified_at:
                    update.middleware.create(i['id'], 'modified', modified_at)
                    hzopg.update_data('release', 'modified_at', "'%s'" % accessed_at, 'id', i['id'])
                if changed_at != last_changed_at:
                    update.middleware.create(i['id'], 'changed', changed_at)
                    hzopg.update_data('release', 'modified_at', "'%s'" % accessed_at, 'id', i['id'])


if __name__ == '__main__':
    main()
