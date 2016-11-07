# -*- coding: UTF-8 -*-

import unittest
from ytcc.download import Download


class TestUpdateOpts(unittest.TestCase):

    opts = {
        'skip_download': True,
        'writeautomaticsub': True
    }

    def setUp(self):
        self.download = Download()

    def test_defaults(self):
        self.assertEqual(self.opts['skip_download'],
                         self.download.opts['skip_download'])

    def test_update_default(self):
        self.download.update_opts({
            'skip_download': False
        })
        self.assertFalse(self.download.opts['skip_download'])

    def test_add_new(self):
        additional = {
            'new_option': 'test'
        }
        self.download.update_opts(additional)
        self.assertEqual('test', self.download.opts['new_option'])
        self.assertEqual(True, self.download.opts['skip_download'])
