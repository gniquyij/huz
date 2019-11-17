# coding: utf-8

import pytest
import sys
sys.path.append('../..')
from utils import hzobe
import settings


cases=[
    ('%s/01.mp3' % settings.HUZ_SRC_PATH, {}),
]


@pytest.mark.parametrize('filename, expectation', cases)
def test_get_metainfo(filename, expectation):
    assert hzobe.get_metainfo(filename) == expectation
