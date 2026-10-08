# -*- coding: UTF-8 -*-

import unittest
from ytcaptions import Download
from unittest.mock import patch, mock_open, Mock
from test.fixtures.webvtt import FIXTURE_WEBVTT, FIXTURE_WEBVTT_STRIPPED


class TestCaptions(unittest.TestCase):

    def test_result(self):
        video_id = 'avoijfsdfa'
        download = Download()
        m = mock_open(read_data=FIXTURE_WEBVTT)

        with patch('ytcaptions.download.open', m, create=True), patch('os.path.exists', return_value=True):
            with patch('ytcaptions.storage.Storage.remove_file', Mock()):
                download.get_result = Mock(return_value=0)
                self.assertEqual(FIXTURE_WEBVTT_STRIPPED,
                                 download.get_captions(video_id))
