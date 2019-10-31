# coding: utf-8

from datetime import datetime
import json
import os
import sys
sys.path.append('..')
import settings
from utils import hzell


def get_stats(src_path):
    accessed_at = datetime.fromtimestamp(os.stat(src_path).st_atime).strftime("%Y-%m-%dT%H:%M:%S")
    modified_at = datetime.fromtimestamp(os.stat(src_path).st_mtime).strftime("%Y-%m-%dT%H:%M:%S")
    changed_at = datetime.fromtimestamp(os.stat(src_path).st_ctime).strftime("%Y-%m-%dT%H:%M:%S")
    return accessed_at, modified_at, changed_at


def update_src_stat(path=settings.HUZ_SRC_PATH):
    srcshot = {}
    srcshot['accessed_at'], srcshot['modified_at'], srcshot['changed_at'] = get_stats(path)
    with open(settings.HUZ_RECORDING_TMP_PATH + '/srcshot.json', 'w') as f:
        json.dump(srcshot, f)


def main():
    with open(settings.HUZ_RECORDING_TMP_PATH + '/srcshot.json') as f:
        srcshot = json.load(f)
        if get_stats(settings.HUZ_SRC_PATH)[0] == srcshot['accessed_at'] and get_stats(settings.HUZ_SRC_PATH)[1] == srcshot['modified_at'] and get_stats(settings.HUZ_SRC_PATH)[2] == srcshot['changed_at']:
            return
    update_src_stat()
    sources = hzell.locate_sources()
    for src in sources:
        src_path = settings.HUZ_SRC_PATH + '/' + src
        accessed_at, modified_at, changed_at = get_stats(src_path)
        with open(settings.HUZ_RECORDING_TMP_PATH + '/dbshot.json') as f:
            dbshot = json.load(f)
            def check_update(stat, field_name, now):
                if now != stat[field_name]:
                    from update.middleware import create_update
                    create_update(stat['id'], field_name, now)
                    from release.middleware import update_release   # TODO: import in the beginning?
                    update_release(stat['id'], field_name, "'%s'" % now)
                    if field_name == 'changed_at':
                        update_release(stat['id'], 'playcount', 'playcount + 1')
                        from album.middleware import update_album
                        update_album(stat['id'], 'playcount', 'playcount + 1')
                        from artist.middleware import update_artist
                        update_artist(stat['id'], 'playcount', 'playcount + 1')
                        from track.middleware import update_track
                        update_track(stat['id'], 'playcount', 'playcount + 1')
                    stat[field_name] = now
            for i in dbshot:
                if i['src_path'] == src_path:
                    check_update(i, 'modified_at', modified_at)
                    check_update(i, 'changed_at', changed_at)
        with open(settings.HUZ_RECORDING_TMP_PATH + '/dbshot.json', 'w') as f:
            json.dump(dbshot, f)


if __name__ == '__main__':
    main()
