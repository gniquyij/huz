# coding: utf-8

import click
import sys
sys.path.append('..')
import settings
from recorders import recording
from utils import hzell, hzopg


def create_table_in_db(cls):
    cls_name = cls.__name__
    c = cls()
    attributes = c.__dict__
    hzopg.create_table(cls_name, attributes)
    return cls


def store_src_info(src_path):
    from release.middleware import create_release, update_release
    release_id, metainfo = create_release(src_path)
    from track.middleware import create_track
    track_id = create_track(metainfo, release_id)[0]
    from album.middleware import create_album
    album_id = create_album(metainfo, release_id)[0]
    from artist.middleware import create_artist
    artist_id = create_artist(metainfo, release_id)[0]
    update_release(release_id, 'track_id', track_id)
    update_release(release_id, 'album_id', album_id)
    update_release(release_id, 'artist_id', artist_id)


@click.group()
def cli():
    pass


@cli.command(help='init/update the database of huz')
@click.option('--option', type=click.Choice(['all', 'src']))
@click.argument('keyword', required=False)
def main(option, keyword=None):
    if option == 'src':
        store_src_info(settings.HUZ_SRC_PATH + '/' + str(keyword))
    else:
        models = hzell.bash_run('find %s -name "models.py"' % settings.HUZ_HOME_PATH).decode('utf-8').split()
        for model in models:
            hzell.bash_run('python %s' % model)
        sources = hzell.locate_sources()
        for src in sources:
            try:
                store_src_info(settings.HUZ_SRC_PATH + '/' + src)
            except:
                continue
    hzopg.dump_data_in_json('id, src_path, accessed_at, modified_at, changed_at', 'release', "'%s/dbshot.json'" % settings.HUZ_RECORDING_TMP_PATH)
    recording.update_src_stat()


if __name__ == '__main__':
    cli()
