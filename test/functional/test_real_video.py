# -*- coding: UTF-8 -*-

import os
import unittest
from ytcc.download import Download, DownloadException


@unittest.skipIf(os.environ.get('CI') == 'true', 'Skip live YouTube network tests in CI (YouTube blocks datacenter IPs)')
class TestRealVideo(unittest.TestCase):

    def setUp(self):
        self.download = Download()

    def test_video(self):
        video_id = 'jNQXAC9IVRw'
        excerpt = 'All right, so here we are, in front of the elephants'
        self.assertEqual(excerpt, self.download.get_captions(
            video_id)[:len(excerpt)])

    def test_video_french(self):
        video_id = 'VLAMC3NJsP4'
        excerpt = "Ah, j'ai fini... Allez, une p’tite partie de LoL !"
        self.assertEqual(excerpt, self.download.get_captions(
            video_id, 'fr')[:len(excerpt)])

    def test_failed(self):
        video_id = '12323123123'
        with self.assertRaises(DownloadException):
            self.download.get_captions(video_id)
