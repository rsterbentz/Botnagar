'''
Hello world

'''

import random

class Player():
    def __init__(self, label, bank):
        self.label = label
        self.bank = bank
        self.bets = {
        'snakeeyes' :0,   # bet for 2         (one roll only)   31:1
        'acedeuce' :0,    # bet for 3         (one roll only)   15:1
        'four' :0,        # bet for 4         (standing)         2:1
        'five' :0,        # bet for 5         (standing)         3:2
        'six' :0,         # bet for 6         (standing)         6:5
        'bigred' :0,      # bet for 7         (one roll only)    4:1
        'eight' :0,       # bet for 8         (standing)         6:5
        'nine' :0,        # bet for 9         (standing)         3:2
        'ten' :0,         # bet for 10        (standing)         2:1
        'yo' :0,          # bet for 11        (one roll only)   15:1
        'boxcars' :0,     # bet for 12        (one roll only)   31:1
        'hard4': 0,       # bet for 2 and 2   (standing)         7:1
        'hard6': 0,       # bet for 3 and 3   (standing)         9:1
        'hard8': 0,       # bet for 4 and 4   (standing)         9:1
        'hard10': 0       # bet for 5 and 5   (standing)         7:1
        }

class Bet():
    def __init__(self, label, ratio, trigger):
        self.label = label
        self.ratio = ratio
        self.trigger = trigger

    def trigger



def snakeeyes():

    if .status == 'PASS':
        if
