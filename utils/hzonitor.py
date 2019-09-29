# coding: utf-8

from datetime import datetime
import json
import os
import sys
sys.path.append('..')
import settings
from utils import hzell


def get_stat(src_path):
    accessed_at = datetime.fromtimestamp(os.stat(src_path).st_atime).strftime("%Y-%m-%dT%H:%M:%S")
    modified_at = datetime.fromtimestamp(os.stat(src_path).st_mtime).strftime("%Y-%m-%dT%H:%M:%S")
    changed_at = datetime.fromtimestamp(os.stat(src_path).st_ctime).strftime("%Y-%m-%dT%H:%M:%S")

    return accessed_at, modified_at, changed_at


def update_src_stat(path=settings.HUZ_SRC_PATH):
    srcshot = {}
    srcshot['accessed_at'], srcshot['modified_at'], srcshot['changed_at'] = get_stat(path)
    with open(settings.HUZ_HZONITOR_TMP_PATH + '/srcshot.json', 'w') as f:
        json.dump(srcshot, f)


def main():
    with open(settings.HUZ_HZONITOR_TMP_PATH + '/srcshot.json') as f:
        srcshot = json.load(f)
        if get_stat(settings.HUZ_SRC_PATH)[0] == srcshot['accessed_at'] and get_stat(settings.HUZ_SRC_PATH)[1] == srcshot['modified_at'] and get_stat(settings.HUZ_SRC_PATH)[2] == srcshot['changed_at']:
            return
    update_src_stat()
    sources = hzell.locate_sources()
    for src in sources:
        accessed_at, modified_at, changed_at = get_stat(settings.HUZ_SRC_PATH + '/' + src)
        with open(settings.HUZ_HZONITOR_TMP_PATH + '/dbshot.json') as f:
            dbshot = json.load(f)
            for i in dbshot:
                def check_update(stat, field_name, now):
                    if now != stat[field_name]:
                        from update.middleware import create
                        create(stat['id'], field_name, now)
                        from release.middleware import update   # TODO: import in the beginning?
                        update(stat['id'], field_name, "'%s'" % now)
                        stat[field_name] = now
                check_update(i, 'accessed_at', accessed_at)
                check_update(i, 'modified_at', modified_at)
                check_update(i, 'changed_at', changed_at)
        with open(settings.HUZ_HZONITOR_TMP_PATH + '/dbshot.json', 'w') as f:
            json.dump(dbshot, f)


if __name__ == '__main__':
    main()
