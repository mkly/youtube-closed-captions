# -*- coding: UTF-8 -*-

import re
import os


class Storage():

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id

    def get_file_path(self) -> str:
        if re.search(r'[^A-z0-9]', self.video_id):
            raise ValueError(
                'Invalid video id attempting to write to filesystem')

        return 'subtitle_{0}.en.vtt'.format(
            re.sub(r'[^A-z0-9]', '', self.video_id))

    def remove_file(self) -> None:
        os.remove(self.get_file_path())
