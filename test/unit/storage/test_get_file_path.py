# -*- coding: UTF-8 -*-

import unittest
from ytcc.storage import Storage


class TestGetFilePath(unittest.TestCase):

    def test_valid(self):
        video_id = 'jNQXAC9IVRw'
        storage = Storage(video_id)
        expected = 'subtitle_{0}.en.vtt'.format(video_id)
        self.assertEqual(expected, storage.get_file_path())

    def test_valid_with_underscore(self):
        video_id = 'w8U6VI_51Bg'
        storage = Storage(video_id)
        expected = 'subtitle_{0}.en.vtt'.format(video_id)
        self.assertEqual(expected, storage.get_file_path())

    def test_valid_with_dash(self):
        video_id = 'x1E0AzpWM-o'
        storage = Storage(video_id)
        expected = 'subtitle_{0}.en.vtt'.format(video_id)
        self.assertEqual(expected, storage.get_file_path())

    def test_invalid(self):
        video_id = 'vsdoi&*@//../../'
        storage = Storage(video_id)
        with self.assertRaises(ValueError):
            storage.get_file_path()
