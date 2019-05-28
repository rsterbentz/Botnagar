import json

class User:
    def __init__(self, nick, bhatnick = False, wallet = 0):
        self.nick = nick
        if bhatnick:
            self.bhatnick = bhatnick
        else:
            self.bhatnick = nick
        self.wallet = wallet
        self.save()
<<<<<<< HEAD

=======
>>>>>>> 7dbe437f02741ab8e9479dbcf0ef3c9a8cc39211
    def save(self):
        dir = 'Users/' + self.nick
        file = open(dir, 'w')
        data = vars(self)
        json.dump(data, file)
        file.close()
<<<<<<< HEAD
        
=======
>>>>>>> 7dbe437f02741ab8e9479dbcf0ef3c9a8cc39211
    def SendCoin(self, other, amt):
        if amt < 0:
            return False
        elif amt > self.wallet:
            return False
        else:
            self.wallet -= amt
            other.wallet += amt
            self.save()
            other.save()

def LoadUser(nick):
    try:
        dir = 'Users/' + nick
        file = open(dir, 'r')
        dict = json.load(file)
        file.close()
        return User(**dict)
    except:
        return False