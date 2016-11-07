# -*- coding: UTF-8 -*-

import unittest
from ytcc.download import Download


class TestRemoveTimeFromCaption(unittest.TestCase):

    caption = '"00:00:49.860 --> 00:00:50.179\nand cook to taste like a hot\ndogs"'
    stripped_caption = "\nand cook to taste like a hot\ndogs"

    caption_two = "'00:00:14.848 --> 00:00:17.350\nMAN:\nWhen we think\nof E equals m c-squared,'"
    stripped_caption_two = "\nMAN:\nWhen we think\nof E equals m c-squared,"

    def setUp(self):
        self.download = Download()

    def test_removal(self):
        self.assertEqual(self.stripped_caption,
                         self.download.remove_time_from_caption(self.caption))

    def test_greedy_newline(self):
        self.assertEqual(
            self.stripped_caption_two,
            self.download.remove_time_from_caption(
                self.caption_two))
