import os
import sys
import unittest

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../")))

import lolreader
from lolreader.utils import camelcase_to_pythonic

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

class TestCamelCase(unittest.TestCase):
    def testcamelcase(self):
        self.assertEqual(camelcase_to_pythonic('weSuckAtLeague'), 'we_suck_at_league')

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = lolreader.read_replay_from_file(PROJECT_PATH + '/test_replays/test.lrf')

    def testversion(self):
        self.assertEqual(self.game.version, 68352)

    def testteams(self):
        self.assertEqual(len(self.game.teams), 2)
        self.assertTrue(self.game.teams[0].won)
        self.assertFalse(self.game.teams[1].won)

    def testplayers(self):
        self.assertEqual(self.game.players[0].summoner, 'Samasdf')

if __name__ == '__main__':
    unittest.main(verbosity=2)
