# Must be run in python 3.4 - 3.6

import discord, random

# Tokens.py contains private discord tokens for beta and release bhat - not in git
import Tokens

# Data.py contains quotes, 8ball responses, and nicknames
from Data import *

# Krypto.py solves integer and fraction Krypto
# Krypto.Main(s) where s is the string of numbers
# n1, n2, n3, n4, n5, target
import Krypto

# Beta switches to beta Botnagar
BETA = False
if BETA:
    TOKEN = Tokens.BETA
else:
    TOKEN = Tokens.RELEASE

def IsPrime(n):
    m=int(n**0.5)
    p=True
    while(m>1 and p==True):
        if(n%m==0):
            p=False
        else:
            m=m-1
    return p

def rolldice():
    a=random.choice([1,2,3,4,5,6])
    b=random.choice([1,2,3,4,5,6])

    if a==1 and b==1:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |         | |     | |         |
        |    O    | |     | |    O    |
        |         | |     | |         |
        |_________|/       \|_________|```'''

    if a==1 and b==2:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |         | |     | |      O  |
        |    O    | |     | |         |
        |         | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==1 and b==3:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |         | |     | |      O  |
        |    O    | |     | |    O    |
        |         | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==1 and b==4:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |         | |     | |  O   O  |
        |    O    | |     | |         |
        |         | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==1 and b==5:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |         | |     | |  O   O  |
        |    O    | |     | |    O    |
        |         | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==1 and b==6:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |         | |     | |  O   O  |
        |    O    | |     | |  O   O  |
        |         | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==2 and b==1:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |         |
        |         | |     | |    O    |
        |  O      | |     | |         |
        |_________|/       \|_________|```'''

    if a==2 and b==2:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |      O  |
        |         | |     | |         |
        |  O      | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==2 and b==3:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |      O  |
        |         | |     | |    O    |
        |  O      | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==2 and b==4:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |  O   O  |
        |         | |     | |         |
        |  O      | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==2 and b==5:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |  O   O  |
        |         | |     | |    O    |
        |  O      | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==2 and b==6:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |  O   O  |
        |         | |     | |  O   O  |
        |  O      | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==3 and b==1:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |         |
        |    O    | |     | |    O    |
        |  O      | |     | |         |
        |_________|/       \|_________|```'''

    if a==3 and b==2:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |      O  |
        |    O    | |     | |         |
        |  O      | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==3 and b==3:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |      O  |
        |    O    | |     | |    O    |
        |  O      | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==3 and b==4:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |  O   O  |
        |    O    | |     | |         |
        |  O      | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==3 and b==5:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |  O   O  |
        |    O    | |     | |    O    |
        |  O      | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==3 and b==6:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |      O  | |     | |  O   O  |
        |    O    | |     | |  O   O  |
        |  O      | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==4 and b==1:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |         |
        |         | |     | |    O    |
        |  O   O  | |     | |         |
        |_________|/       \|_________|```'''

    if a==4 and b==2:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |      O  |
        |         | |     | |         |
        |  O   O  | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==4 and b==3:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |      O  |
        |         | |     | |    O    |
        |  O   O  | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==4 and b==4:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==4 and b==5:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |         | |     | |    O    |
        |  O   O  | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==4 and b==6:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |         | |     | |  O   O  |
        |  O   O  | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==5 and b==1:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |         |
        |    O    | |     | |    O    |
        |  O   O  | |     | |         |
        |_________|/       \|_________|```'''

    if a==5 and b==2:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |      O  |
        |    O    | |     | |         |
        |  O   O  | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==5 and b==3:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |      O  |
        |    O    | |     | |    O    |
        |  O   O  | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==5 and b==4:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |    O    | |     | |         |
        |  O   O  | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==5 and b==5:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |    O    | |     | |    O    |
        |  O   O  | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==5 and b==6:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |    O    | |     | |  O   O  |
        |  O   O  | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==6 and b==1:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |         |
        |  O   O  | |     | |    O    |
        |  O   O  | |     | |         |
        |_________|/       \|_________|```'''

    if a==6 and b==2:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |      O  |
        |  O   O  | |     | |         |
        |  O   O  | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==6 and b==3:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |      O  |
        |  O   O  | |     | |    O    |
        |  O   O  | |     | |  O      |
        |_________|/       \|_________|```'''

    if a==6 and b==4:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |  O   O  | |     | |         |
        |  O   O  | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==6 and b==5:
        msg = '''```   _________       _________
         /________ /|     |\ ________\
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |  O   O  | |     | |    O    |
        |  O   O  | |     | |  O   O  |
        |_________|/       \|_________|```'''

    if a==6 and b==6:
        msg = '''```   _________       _________
         /________ /|     |\ ________\ 
        |         | |     | |         |
        |  O   O  | |     | |  O   O  |
        |  O   O  | |     | |  O   O  |
        |  O   O  | |     | |  O   O  |
        |_________|/       \|_________|```'''

    return msg

client = discord.Client()

@client.event
async def on_message(message):
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return

    # This block determines nickname of AUTHOR
    if str(message.author)[:-5] in users:
        AUTHOR = users[str(message.author)[:-5]]
    else:
        AUTHOR = str(message.author)[:-5]


    # Bhat can interject in any channel
    if 'bhat' in message.content.lower() and not message.content.startswith('!bhat'):
        msg = random.choice([
        '*Did somebody say my name?*',
        '*Hello my studnets!*',
        '*HERE I AM!*',
        '*I have arrived!*',
        '*I do believe {AUTHOR} rang?*'.format(AUTHOR = AUTHOR),
        '*Hello, {AUTHOR}!*'.format(AUTHOR = AUTHOR),
        '*Yes?*',
        '*Err...*'])
        await client.send_message(message.channel, msg)

    # Beta build only posts in beta-bhatnagar
    elif BETA == True and str(message.channel) != 'beta-botnagar-fanfic':
        return

    # standard build only posts in bhatnagar
    elif BETA == False and str(message.channel) != 'botnagar-fanfic':
        return

    elif message.content.startswith('!bhat 8ball'):
        msg = random.choice(ball).format(AUTHOR = AUTHOR)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!bhat quote'):
        randcomposite = random.randint(3, 100)
        while IsPrime(randcomposite):
            randcomposite = random.randint(3, 100)
        msg = random.choice(quotes).format(AUTHOR = AUTHOR, randcomposite = randcomposite) # random.choice(quotes) returns a string,
        await client.send_message(message.channel, msg)     # so then .format(AUTHOR = AUTHOR) replaces the {} in the string

    elif message.content.startswith('!bhat hello'):
        msg = '*Hello, {AUTHOR}!*'.format(AUTHOR = AUTHOR)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!bhat roll'): # working out the details, won't look this messy for long.
        msg = rolldice()
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!bhat info'):
        MaxPlayer = max(PrimeScore, key = PrimeScore.get)
        n1 = random.randint(1, 99)
        n2 = random.randint(0, 9)
        n3 = random.randint(0, 9)
        n4 = random.randint(1, 99)
        msg = '''*Hello, {AUTHOR}! I am your tenured virtual professor, Botnagar! (ver {n1}.{n2}.{n3}:{n4})
Below is a list of commands that I may be doing them!*

    - !bhat quote *[I can tell you something juicy!]*
    - !bhat 8ball *[I enjoy giving out my advices for you!]*
    - !bhat prime *[I\'ll give you a prime. Let\'s see if it\'s a big one!]*
    - !bhat primescore *[Who\'s winning? Right now it\'s {MaxPlayer}!]*
    - !bhat hello *[Say hi! Don't be afraid!]*
    - !bhat roll *[Roll some number cubes! How fun!]*
    - !bhat krypto *[Maybe you can't solve this one? Give me 6 numbers like this n1, n2, n3, n4, n5, target]*'''
        msg = msg.format(AUTHOR = AUTHOR, MaxPlayer = MaxPlayer, n1 = n1, n2 = n2, n3 = n3 , n4 =n4)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!bhat primescore'):
        MaxPlayer = max(PrimeScore, key = PrimeScore.get)
        response1 = random.choice([
        '*Here is the board of SCORES!*',
        '*Do you know... these are all PRIMES?*',
        '*I believe this is what you might be of the looking for it?*',
        '*You know, this board contains the SCORES!*',
        '*These are of the scores of it! Yes!*'
        ])

        response2 = '\n'
        for p in PrimeScore:
            response2 = response2 + '*{} -- {}* \n'.format(p, PrimeScore[p])

        response3 = random.choice([
        '*{MaxPlayer} appears to be the winning of it!*',
        '*I think the prime held by {MaxPlayer} is the winner!*',
        '*You know {MaxPlayer}, you ARE a winner!*',
        '*Did you know that 60\% of winners are named {MaxPlayer}??*',
        '*Wow {MaxPlayer}! You ARE the winner! Yes!*'
        ])

        msg = response1 + response2 + response3
        msg = msg.format(MaxPlayer = MaxPlayer)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!bhat prime'):
        prime = 2
        while True:
            if IsPrime(prime) == True:
                if random.random() <= .05:
                    final = prime
                    break
            if prime == 2:
                prime = 3
            else:
                prime = prime+2

        MaxPlayer = max(PrimeScore, key = PrimeScore.get)
        MaxPrime = PrimeScore[MaxPlayer]

        if final > MaxPrime:
            PrimeScore[AUTHOR] = final
            msg = random.choice([
            '*Wow! {AUTHOR}, your prime {final} is the twinkle of my eye!*',
            '*Oh my! {AUTHOR} got the prime {final}! Now here is something very amazing thing!*',
            '*{AUTHOR}, look! You\'ve recieved a tremendous prime of {final}!*',
            '*Everybody look at this! {AUTHOR} has obtained the most massive prime {final}!*',
            '*How incredible! {AUTHOR}\'s prime of {final} is the highest one I\'ve seen of it!*',
            '*{AUTHOR} just got the prime {final}! This is the largest prime most probably!*',
            '*Is {AUTHOR}\'s prime of the {final} the largest of the primes? ...Yes!*'
            ])

        else:
            if final > PrimeScore[AUTHOR]:
                PrimeScore[AUTHOR] = final
            msg = random.choice([
            '*{AUTHOR}, your prime is {final}! ',
            '*{AUTHOR} may have the prime {final}! ',
            '*I will give {AUTHOR} the prime {final}! ',
            '*{final} is the prime by which you may be HAVING it... {AUTHOR}! ',
            '*Here is your prime, {AUTHOR}... (drops {final} from hand) ',
            '*The prime {final} goes to.... err... \"{AUTHOR}\"....? '
            ])+'{MaxPlayer} still has the largest prime of {MaxPrime}!*'

        msg = msg.format(AUTHOR = AUTHOR, final = final, MaxPlayer = MaxPlayer, MaxPrime = MaxPrime)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!bhat krypto'):
        s = str(message.content)[12:]
        Solution = Krypto.Main(s)

        if Solution == False:
            msg = random.choice([
            '*I\'m awfully sorry, {AUTHOR}, I couldn\'t find a soltuion*',
            '*Err... I guess this one of the ones that cannot be of the solving it!*'
            ])
            await client.send_message(message.channel, msg.format(AUTHOR = AUTHOR))
        else:
            msg = random.choice([
            '*Aha! I have your solution {AUTHOR}!* \n',
            '*Looking for this now?* \n'
            ])
            msg = msg + '```' + Solution + '```'
            await client.send_message(message.channel, msg.format(AUTHOR = AUTHOR))

    elif message.content.startswith('!bhat'):
        msg = random.choice([
        '*So... err...*',
        '*I\'m not sure I know what this is, {AUTHOR}.*'.format(AUTHOR = AUTHOR),
        '*Err... this is one of the things of which I do not know.... it!*'])
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name = '...it!'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
