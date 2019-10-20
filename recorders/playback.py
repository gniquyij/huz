# coding: utf-8

import sys
sys.path.append('..')
import stats.middleware
from stats.models import AlbumStats
from stats.models import ArtistStats
from stats.models import UpdateStats
from stats.models import ReleaseStats
from stats.models import TrackStats


def main():
    stats.middleware.create(ReleaseStats, 'ReleaseCount')
    stats.middleware.create(AlbumStats, 'AlbumCount')
    stats.middleware.create(ArtistStats, 'ArtistCount')
    stats.middleware.create(TrackStats, 'TrackCount')
    stats.middleware.create(UpdateStats, 'UpdateCount')


if __name__ == '__main__':
    main()
