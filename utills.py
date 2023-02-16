from objekt import BasicWord
import requests
from random import randint
from player_1 import Player


def load_random_word():
    i = requests.get('https://jsonkeeper.com/b/1NVT', verify=False).json()
    random_num = randint(0, len(i) - 1)
    word = BasicWord(i[random_num]["word"], i[random_num]["subwords"])
    return word


def statistic_game():
    q = Player()
    return q
