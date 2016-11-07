# -*- coding: UTF-8 -*-

import unittest
from ytcc.storage import Storage
from unittest.mock import patch


class TestRemoveFile(unittest.TestCase):

    @patch('os.remove')
    def test_remove_file(self, mock):
        video_id = 'v2309jfGew'
        file_path = 'subtitle_v2309jfGew.en.vtt'
        storage = Storage(video_id)
        storage.remove_file()
        mock.assert_called_with(file_path)
