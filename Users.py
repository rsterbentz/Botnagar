import json
import os

# List of all users with accounts
ActiveUsers = []

# Where user data is stored
UserDataDirectory = 'Userdata/'

# Create folder if nonexistent
if not os.path.exists(UserDataDirectory):
    os.makedirs(UserDataDirectory)

class User:
    def __init__(self, nick, bhatnick = False, wallet = 0, **kwargs):

        # nick - discord nickname in server
        self.nick = nick

        # bhatnick - name given by bhat
        if bhatnick:
            self.bhatnick = bhatnick
        else:
            self.bhatnick = nick
        self.wallet = wallet

        # In case extra variables are stored
        self.__dict__.update(kwargs)
        self.save()

    def save(self):
        dir = UserDataDirectory + self.nick
        file = open(dir, 'w')
        data = vars(self)
        json.dump(data, file)
        file.close()

    def sendCoin(self, other, amt):
        # Negative coins reverses transaction
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
    global ActiveUsers
    try:
        dir = UserDataDirectory + nick
        file = open(dir, 'r')
        dict = json.load(file)
        file.close()
        ActiveUsers.append(User(**dict))
    except:
        return False