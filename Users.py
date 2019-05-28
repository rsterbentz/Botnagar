import json

class User:
    def __init__(self, nick, bhatnick = False, wallet = 0, **kwargs):
        self.nick = nick
        if bhatnick:
            self.bhatnick = bhatnick
        else:
            self.bhatnick = nick
        self.wallet = wallet
        self.__dict__.update(kwargs)
        self.save()

    def save(self):
        dir = 'Users/' + self.nick
        file = open(dir, 'w')
        data = vars(self)
        json.dump(data, file)
        file.close()

    def sendCoin(self, other, amt):
        if amt < 0:
            return False
        elif amt > self.wallet:
            return False
        else:
            self.wallet -= amt
            other.wallet += amt
            self.save()
            other.save()

def loadUser(nick):
    try:
        dir = 'Users/' + nick
        file = open(dir, 'r')
        dict = json.load(file)
        file.close()
        return User(**dict)
    except:
        return False