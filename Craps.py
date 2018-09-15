'''
-------------
Craps outline
-------------

1 - Create player database
2 - Take bets & store into....classes..?
    - Lock bet into class
    - Ready check
3 - Roll dice
4 - Determine winners & loosers
5 -

-----
Notes
-----

-- Include recurring bets

RATIOS:



--------
Commands
--------


'''

import random

PUCK = 'OFF'

# Structure: 'label': (<ratio as float>, <standing/one-time>)
BetTypes = {
    'snakeeyes': (31/1, 'one-time'),
    'acedeuce':  (15/1, 'one-time'),
    'four':      (2/1, 'standing'),
    'five':      (3/2, 'standing'),
    'six':       (6/5, 'standing'),
    'bigred':    (4/1, 'one-time'),
    'eight':     (6/5, 'standing'),
    'nine':      (3/2, 'standing'),
    'ten':       (2/1, 'standing'),
    'yo':        (15/1, 'standing'),
    'boxcars':   (31/1, 'one-time'),
    'hard4':     (7/1, 'standing'),
    'hard6':     (9/1, 'standing'),
    'hard8':     (9/1, 'standing'),
    'hard10':    (7/1, 'standing')
}


players = {}

class Bet:
    def __init__(self, type, amt):
        self.type = type
        self.amt = amt


class Player:
    def __init__(self, bank, name):
        self.bank = bank
        self.name = name
        self.bets = []

    def bet(self, type, amt):
        # Don't make bets too large
        if amt > self.bank:
            return False

        b = Bet(type = type, amt = amt)
        self.bets.append(b)
        self.bank = self.bank - amt

    def leavegame(self):
        for b in self.bets:
            self.bank = self.bank + b.amt
        self.bets = []
