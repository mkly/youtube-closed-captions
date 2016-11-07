# -*- coding: UTF-8 -*-

import unittest
from ytcc.download import Download


class TestDownloadGetUrlFromVideoId(unittest.TestCase):

    def setUp(self):
        self.download = Download()

    def test_set(self):
        video_id = 'vDOIDJdds'
        test = 'http://www.youtube.com/watch?v={0}'.format(video_id)
        result = self.download.get_url_from_video_id(video_id)
        self.assertEqual(test, result)

    def test_encoding(self):
        video_id = 'vDDD://'
        encoded_video_id = 'vDDD%3A%2F%2F'
        test = 'http://www.youtube.com/watch?v={0}'.format(encoded_video_id)
        result = self.download.get_url_from_video_id(video_id)
        self.assertEqual(test, result)
