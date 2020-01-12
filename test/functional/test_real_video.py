# -*- coding: UTF-8 -*-

import unittest
from ytcc.download import Download, DownloadException


class TestRealVideo(unittest.TestCase):

    def setUp(self):
        self.download = Download()

    def test_video(self):
        video_id = 'jNQXAC9IVRw'
        excerpt = 'All right, so here we are in front of the elephants, the cool thing'
        self.assertEqual(excerpt, self.download.get_captions(
            video_id)[:len(excerpt)])

    def test_video_french(self):
        video_id = 'VLAMC3NJsP4'
        excerpt = 'J\'ai fini Jouons à LoL (League of Legends). Oh mon Dieu,'
        self.assertEqual(excerpt, self.download.get_captions(
            video_id, 'fr')[:len(excerpt)])

    def test_failed(self):
        video_id = '12323123123'
        with self.assertRaises(DownloadException):
            self.download.get_captions(video_id)
