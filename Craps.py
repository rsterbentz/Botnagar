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

players = {}

class Bet:
    def __init__(self, label, amt, ratio, one-time = False):
        pass

class Player:
    def __init__(self, bank, label):
        self.bank = bank
        self.label = label                                    # Pass  # Don't Pass
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



    def __str__(self):
        s = '{name} has ${bank}'.format(name = self.label, bank = self.bank)
        return s

    def bet(self, type, amt):
        # Don't make bets too large
        if amt > self.bank:
            return False

        self.bets[type] = amt
        self.bank = self.bank - amt

        for bet in self.bets:
            if self.bets[bet] < 0:
                self.bets[bet] = 0

    def payout(self, roll):
        # roll is the number shown on dice
        # roll is a tuple (d1, d2)
        pay = 0
        if

    def leavegame(self):
        pass





p1 = Player(bank = 100, label = 'Thomas')
^^^^
p2 = Player(bank = 5, label = 'Harrison')

str(4) - '4'

p2.add1000()

str(12) -> '12'

p1.bank -> 100
p2.bank -> 5

players = []
players.append(  player(bank = 100, label = 'Thomas') )

Thomas.bank -> 100
