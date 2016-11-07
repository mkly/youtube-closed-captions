# -*- coding: UTF-8 -*-

import unittest
from ytcc.download import Download
from test.fixtures.webvtt import FIXTURE_WEBVTT, FIXTURE_WEBVTT_STRIPPED


class TestGetFilePathFromVideoId(unittest.TestCase):

    def setUp(self):
        self.download = Download()

    def test_valid(self):
        self.assertEqual(
            FIXTURE_WEBVTT_STRIPPED,
            self.download.get_captions_from_output(FIXTURE_WEBVTT))
