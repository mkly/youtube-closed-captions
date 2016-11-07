# -*- coding: UTF-8 -*-

import unittest
from ytcc.download import Download
from unittest.mock import patch, Mock


class TestGetResult(unittest.TestCase):

    def test_result_is_zero(self):
        video_id = 'we342oij234'
        ydl = Mock()
        ydl.download = Mock(return_value=0)

        with patch('youtube_dl.YoutubeDL.__enter__', return_value=ydl):
            download = Download()
            self.assertEqual(0, download.get_result(video_id))
            ydl.download.assert_called_with(
                ['http://www.youtube.com/watch?v=we342oij234'])
