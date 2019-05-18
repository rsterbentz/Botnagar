#!/usr/bin/python3
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

# Used for !bhat craps
# Still in development
import Craps

# Beta switches to beta Botnagar
BETA = False
if BETA:
    TOKEN = Tokens.BETA
else:
    TOKEN = Tokens.RELEASE

def containsNumbers(s):
    return any(character.isdigit() for character in s)

def IsPrime(n):
    m=int(n**0.5)
    p=True
    while(m>1 and p==True):
        if(n%m==0):
            p=False
        else:
            m=m-1
    return p

def factor(n):
    factors = set()
    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
    l = list(factors)
    l.sort()
    return l

# Counts the number of numbers in msg
# and saves data to Benford.dat
def BenfordCount(msg):

        # Try to open the file. If not, build file.
        try:
            BenfordFile = open('Benford.dat', 'r')

            # Take data from file and transfer to list
            RawData = BenfordFile.readlines()
            BenfordFile.close()
        except:
            BenfordFile = open('Benford.dat', 'w')
            BenfordFile.write('0:0\n1:0\n2:0\n3:0\n4:0\n5:0\n6:0\n7:0\n8:0\n9:0\n')
            BenfordFile.close()

            # Take data from file and transfer to list
            BenfordFile = open('Benford.dat', 'r')
            RawData = BenfordFile.readlines()
            BenfordFile.close()

        # Take raw data and turn into list
        BenfordData = []
        for x in RawData:
            s = str(x)[2:-1]
            BenfordData.append(int(s))

        # Look for integer i in message, add count to BenfordData
        for i in range(10):
            count = msg.count(str(i))
            BenfordData[i] = BenfordData[i] + count

        # Convert Benford data back into string
        s = ''
        for i in range(10):
            s = s + '{}:{}\n'.format(i, BenfordData[i])

        # Save data back to Benford.dat
        BenfordFile = open('Benford.dat', 'w')
        BenfordFile.write(s)
        BenfordFile.close()


# Roll 2 dice at random - used for !bhat roll
def rolldice():
    a=random.choice([1,2,3,4,5,6])
    b=random.choice([1,2,3,4,5,6])

    # Build framework for dice
    msg = (
    '```'
    '\n   _________       _________'
    '\n /________ /|     |\ ________\\'
    '\n|         | |     | |         |'
    '\n|  {a1}   {a5}  | |     | |  {b1}   {b5}  |'
    '\n|  {a2} {a4} {a6}  | |     | |  {b2} {b4} {b6}  |'
    '\n|  {a3}   {a7}  | |     | |  {b3}   {b7}  |'
    '\n|_________|/       \|_________|'
    '```'
    )

    # Create determine which pip structure to use
    pips = {
    1:(' ', ' ', ' ', 'O', ' ', ' ', ' '),
    2:(' ', ' ', 'O', ' ', 'O', ' ', ' '),
    3:(' ', ' ', 'O', 'O', 'O', ' ', ' '),
    4:('O', ' ', 'O', ' ', 'O', ' ', 'O'),
    5:('O', ' ', 'O', 'O', 'O', ' ', 'O'),
    6:('O', 'O', 'O', ' ', 'O', 'O', 'O')
    }

    # Unpack pips into single variable
    (a1, a2, a3, a4, a5, a6, a7) = pips[a]
    (b1, b2, b3, b4, b5, b6, b7) = pips[b]

    # Push pips to framework
    msg = msg.format(a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5, a6 = a6, a7 = a7, b1 = b1, b2 = b2, b3 = b3, b4 = b4, b5 = b5, b6 = b6, b7 = b7)
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

    # Benford's Law code
    # Check if string contains numbers
    if containsNumbers( str(message.content) ):
        BenfordCount( str(message.content) )

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

    # Bhat other interjections
    if 'history' in message.content.lower() and not message.content.startswith('!bhat'):
        msg = random.choice([
        '*I remember when I taught the history of...err...*',
        '*I once taught a, err, history class..*',
        '*HISTORY is my passion, {AUTHOR}!*'.format(AUTHOR = AUTHOR)])
        await client.send_message(message.channel, msg)

    # Bhat other interjections
    if 'tenure' in message.content.lower() and not message.content.startswith('!bhat'):
        msg = random.choice([
        '*Did you know I have DENURE??*',
        '*Most professors don\'t get TENURE, you know {AUTHOR}*'.format(AUTHOR = AUTHOR)])
        await client.send_message(message.channel, msg)

    # Bhat other interjections
    if 'book' in message.content.lower() and not message.content.startswith('!bhat'):
        msg = random.choice([
        '*You know, I have written many books..yes..*',
        '*You know, there are many DARTS in my book, yes!*',
        '*Have you BHAT my book yet, {AUTHOR}??*'.format(AUTHOR = AUTHOR)])
        await client.send_message(message.channel, msg)

    # standard build only posts in bhatnagar
    elif BETA == False and (str(message.channel) != 'botnagar' or str(message.channel) != 'botnagar-workshop'):
        return

    # Bhat 8ball roller
    elif message.content.startswith('!bhat 8ball'):
        msg = random.choice(ball).format(AUTHOR = AUTHOR)
        await client.send_message(message.channel, msg)

    # Bhat random quote
    elif message.content.startswith('!bhat quote'):
        randcomposite = random.randint(3, 100)
        while IsPrime(randcomposite):
            randcomposite = random.randint(3, 100)
        msg = random.choice(quotes).format(AUTHOR = AUTHOR, randcomposite = randcomposite) # random.choice(quotes) returns a string,
        await client.send_message(message.channel, msg)     # so then .format(AUTHOR = AUTHOR) replaces the {} in the string

    # bhat hello command
    elif message.content.startswith('!bhat hello'):
        msg = '*Hello, {AUTHOR}!*'.format(AUTHOR = AUTHOR)
        await client.send_message(message.channel, msg)

    # Bhat roll 2 dice
    elif message.content.startswith('!bhat roll'):
        msg = rolldice()
        await client.send_message(message.channel, msg)

    # Bhat gives info on commands
    elif message.content.startswith('!bhat info'):
        MaxPlayer = max(PrimeScore, key = PrimeScore.get)
        n1 = random.randint(1, 99)
        n2 = random.randint(0, 9)
        n3 = random.randint(0, 9)
        n4 = random.randint(1, 99)
        msg = (
        '*Hello, {AUTHOR}! I am your tenured virtual professor, Botnagar! (ver {n1}.{n2}.{n3}:{n4})'
        '\nBelow is a list of commands that I may be doing them!*'
        '\n'
        '\n    - !bhat quote *[I can tell you something juicy!]*'
        '\n    - !bhat 8ball *[I enjoy giving out my advices for you!]*'
        '\n    - !bhat prime *[I\'ll give you a prime. Let\'s see if it\'s a big one!]*'
        '\n    - !bhat primescore *[Who\'s winning? Right now it\'s {MaxPlayer}!]*'
        '\n    - !bhat hello *[Say hi! Don\'t be afraid!]*'
        '\n    - !bhat roll *[Roll some number cubes! How fun!]*'
        '\n    - !bhat krypto *[Maybe you can\'t solve this one? Give me 6 numbers like this n1, n2, n3, n4, n5, target]*'
        )
        msg = msg.format(AUTHOR = AUTHOR, MaxPlayer = MaxPlayer, n1 = n1, n2 = n2, n3 = n3, n4 = n4)
        await client.send_message(message.channel, msg)

    # Bhat gives the current primes
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

    # Bhat checks if a number is prime
    elif message.content.startswith('!bhat primecheck'):
        l = message.content.split()
        n = eval(l[2])
        if IsPrime(n) or random.random() <= .01:
            msg = random.choice([
                '*I do believe {n} is :b:rime!!*',
                '*Did you know, {AUTHOR}, that {n} is the largest :b:rime?*'
            ])
        else:
            msg = random.choice([
                '*{AUTHOR}, give me 7 to 9 nuggets on why {n} is not prime.. These ARE the factors!*',
                '*Err, {n} may be of the primes, but it is not! It has these factors!*'
            ])
        msg = msg.format(AUTHOR = AUTHOR, n = n)
        msg = msg + '\n' + str(factor(n))
        await client.send_message(message.channel, msg)

    # Bhat gives you a prime and adds to primescore
    elif message.content.startswith('!bhat prime'):
        prime = 2
        while True:
            if IsPrime(prime) == True:
                if random.random() <= .05:
                    final = prime
                    if random.random() <= .1:
                        final = final + 2
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

    # Bhat krypto solver
    elif message.content.startswith('!bhat krypto'):
        s = str(message.content)[12:]
        Solution = Krypto.Main(s)

        if Solution == False:
            msg = random.choice([
            '*I\'m awfully sorry, {AUTHOR}, I couldn\'t find a solution*',
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
