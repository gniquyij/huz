# coding: utf-8

import sys
sys.path.append('..')
import stats.middleware
from stats.models import ReleaseStats
from stats.models import AlbumStats
from stats.models import ArtistStats
from stats.models import TrackStats


def main(dur):
    stats.middleware.create(ReleaseStats, dur)
    stats.middleware.create(AlbumStats, dur)
    stats.middleware.create(ArtistStats, dur)
    stats.middleware.create(TrackStats, dur)


if __name__ == '__main__':
    main(sys.argv[1])
