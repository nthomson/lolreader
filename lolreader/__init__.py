import urllib2
from lolreader.objects import Game

def read_replay_from_file(replay_file):
    with open(replay_file, 'r') as replay:
        return Game(replay)

def read_replay_from_url(replay_url):
    replay = urllib2.urlopen(replay_url)

    return Game(replay)
