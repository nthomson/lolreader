from lolreader import Game

def read_replay_from_file(replay_file):
    with open(replay_file, 'r') as replay:
        return Game(replay)

def read_replay_from_url(replay_url):
    replay = urllib2.urlopen(replay_url)

    return Game(replay)

def camelcase_to_pythonic(word):
    char_list = list(word)
    for counter, c in enumerate(char_list):
        if(c.isupper()):
            char_list.insert(counter, '_')
            if char_list[counter + 1]:
                char_list[counter + 1] = char_list[counter + 1].lower()

    return ''.join(char_list)
