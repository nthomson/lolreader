import struct, json, sys, urllib2
from utils import camalcase_to_pythonic

def read_replay_from_file(replay_file):
    with open(replay_file, 'r') as replay:
        return LoLReader(replay)

def read_replay_from_url(replay_url):
    replay = urllib2.urlopen(replay_url)

    return LoLReader(replay)

class LoLReader(object):
    # version of LoLReplay client
    version = int()

    # length of reply metadata
    meta_length = int()

    # replay meta data (aka. everything we care about)
    meta_data = dict()

    # list of teams in the replay
    teams = list()

    # list of players in the replay
    players = list()

    def __init__(self, replay):
        self.version, self.meta_length = struct.unpack('ii', replay.readline(8))
        self.meta_data = json.loads(replay.readline(self.meta_length))

        self.teams = [Team(x) for x in range(1, 3)]
        self.players = [Player(player) for player in self.meta_data['players']] 

        for team in self.teams:
            team.players = [player for player in self.players if player.team == team.number]
            team.is_winner = team.players[0].won

class Team(object):
    number = int()
    players = list()
    is_won = False

    def __init__(self, number):
        self.number = number

class Player(object):
    """
    gold = int()
    deaths = int()
    healed = int()
    magic_damage_taken = int()
    summoner = str()
    profile_icon_id = int()
    item1 = int()
    item2 = int()
    item3 = int()
    item4 = int()
    item5 = int()
    item6 = int()
    won = False
    spell2 = int()
    account_id = int()
    magic_damage_dealt = int()
    champion = str()
    kills = int()
    damage_taken = int()
    summoner_level = int()
    assists = int()
    neutral_minions_killed = int()
    spell1 = int()
    minions = int()
    level = int()
    wins = int()
    leaves = int()
    losses = int()
    damage_dealt = int()
    physical_damage_dealt = int()
    team = int()
    physical_damage_taken = int()
    time_dead = int()
    """

    def __init__(self, raw_data):
        # so... this is probably a security flaw
        for attribute in raw_data.keys():
            vars(self)[camalcase_to_pythonic(attribute)] = raw_data[attribute]