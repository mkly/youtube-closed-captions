# -*- coding: UTF-8 -*-

import yt_dlp as youtube_dl
from pycaption import WebVTTReader
import os
import re
from urllib.parse import urlencode
from ytcc.storage import Storage
from ytcc.fake_logger import FakeLogger


class Download():
    base_url = 'http://www.youtube.com/watch'

    def __init__(self, opts: dict = {}) -> None:
        self.opts = {
            'skip_download': True,
            'writeautomaticsub': True,
            'writesubtitles': True,
            'subtitlesformat': 'vtt',
            'outtmpl': 'subtitle_%(id)s',
            'logger': FakeLogger()
        }
        self.opts.update(opts)

    def update_opts(self, opts: dict) -> None:
        self.opts.update(opts)

    def get_captions(self, video_id: str, language: str = 'en') -> str:
        result = self.get_result(video_id, language)

        if result != 0:
            raise DownloadException(
                'Unable to download and extract captions: {0}'.format(result))

        storage = Storage(video_id, language)
        file_path = storage.get_file_path()
        if not os.path.exists(file_path):
            raise DownloadException(
                'No closed captions found for video {0} in language {1}'.format(video_id, language))

        with open(file_path, 'r', encoding='utf-8') as f:
            output = self.get_captions_from_output(f.read(), language)
        storage.remove_file()
        return output

    def get_result(self, video_id: str, language: str = 'en') -> int:
        opts = self.opts.copy()
        if language:
            opts['subtitleslangs'] = list(dict.fromkeys([*opts.get('subtitleslangs', []), language]))

        with youtube_dl.YoutubeDL(opts) as ydl:
            try:
                return ydl.download([self.get_url_from_video_id(video_id)])
            except youtube_dl.utils.DownloadError as err:
                raise DownloadException(
                    "Unable to download captions: {0}".format(str(err)))
            except youtube_dl.utils.ExtractorError as err:
                raise DownloadException(
                    "Unable to extract captions: {0}".format(str(err)))
            except Exception as err:
                raise DownloadException(
                    "Unknown exception downloading and extracting captions: {0}".format(
                        str(err)))


    def get_url_from_video_id(self, video_id: str) -> str:
        return '{0}?{1}'.format(self.base_url, urlencode({'v': video_id}))

    def get_captions_from_output(self, output: str, language: str = 'en') -> str:
        reader = WebVTTReader()

        temp_final = ''
        for caption in reader.read(output, language).get_captions(language):
            stripped = self.remove_time_from_caption(
                str(caption).replace(r'\n', "\n"))
            temp_final += stripped

        final = ''
        previous = ''
        for line in temp_final.split("\n"):
            if previous != line:
                final += "\n" + line
            previous = line

        return final.replace("\n", ' ')[1:]

    def remove_time_from_caption(self, caption: str) -> str:
        caption = caption[1:-1]
        return re.sub(r"^.*?\n", "\n", caption)


class DownloadException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
