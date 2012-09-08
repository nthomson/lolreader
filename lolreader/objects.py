import struct
import json
from utils import camelcase_to_pythonic

class Game(object):
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
    
    # information about the game
    match_type = int()
    game_mode = int()
    queue_type = str()
    region = str()
    ranked = False
    match_length = int()
    timestamp = int()

    def __init__(self, replay):
        self.version, self.meta_length = struct.unpack('ii', replay.readline(8))
        self.meta_data = json.loads(replay.readline(self.meta_length))

        self.teams = [Team(x) for x in range(1, 3)]
        self.players = [Player(player) for player in self.meta_data['players']] 

        self.match_type = self.meta_data['match_type']
        self.game_mode = self.meta_deta['game_mode']
        self.queue_type = self.meta_data['queue_type']
        self.region = self.meta_data['region']
        self.ranked = self.meta_data['ranked']
        self.match_length = self.meta_data['match_length']
        self.timestamp = self.meta_data['timestamp']

        for team in self.teams:
            team.players = [player for player in self.players if player.team == team.number]
            team.won = team.players[0].won

class Team(object):
    number = int()
    players = list()
    won = False

    def __init__(self, number):
        self.number = number

class Player(object):
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
    killing_spree = int()
    turrets = int()
    barracks = int()

    def __init__(self, raw_data):
        # so... this is probably a security flaw
        for attribute in raw_data.keys():
            vars(self)[camelcase_to_pythonic(attribute)] = raw_data[attribute]
