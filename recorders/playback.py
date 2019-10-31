# coding: utf-8

import sys
sys.path.append('..')
from stats.middleware import create_stats
from stats.models import AlbumStats
from stats.models import ArtistStats
from stats.models import UpdateStats
from stats.models import ReleaseStats
from stats.models import TrackStats


def main():
    create_stats(ReleaseStats, 'ReleaseCount')
    create_stats(AlbumStats, 'AlbumCount')
    create_stats(ArtistStats, 'ArtistCount')
    create_stats(TrackStats, 'TrackCount')
    create_stats(UpdateStats, 'UpdateCount')


if __name__ == '__main__':
    main()
