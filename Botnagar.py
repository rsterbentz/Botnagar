# Must be run in python 3.4 - 3.6

import discord
import random
# import Krypto
# ^Uncomment if you have Krypto.py

BETA = False

if BETA:
    TOKEN = 'NDg0NzYxNjEyMzg1OTEwODE2.DnUK_w.btd6vRc3t36KR28AtogTfEdcYQ4'
else:
    TOKEN = 'NDg0NzYwMDUwODQ2NDAwNTMz.DnUjsA.pCWU_VhR0TKRGQoK1zF6EWWOK_I'

client = discord.Client()

users = {
'Porsche':'Dom',
'Jumping Dog':'Etin Window',
'Renskay':'Etin Spyder',
'Tovar':'Rodger',
'yolomaster':'Garry',
'Desk':':b: :regional_indicator_r: :regional_indicator_e: :regional_indicator_a: :regional_indicator_d:',
'tuxy':':b: oston'
}

quotes = [
'*You know, {AUTHOR}, there is so much to look around!*',
'*Yes, {AUTHOR}, this is really the real substance of life!*',
'*Unfortunately, {AUTHOR}, there is no fanciful term we can use for this!*',
'*{AUTHOR}, I want you to think about this that you are saying... it.*',
'*If you think about it, {AUTHOR}, so many people came and went away.*',
'*You know, {AUTHOR}, that is something that you will have your stamp on it!*',
'*You know, {AUTHOR}, not all of them do, but they will.*',
'*Watch my remarks, {AUTHOR}.*',
'*{AUTHOR}, I saw a twinkle in my eye!*',
'*{AUTHOR}, please give me three or five lines of gist on it.*',
'*{AUTHOR}, today I want you to set the bar rolling!*',
'*Unfortunately, {AUTHOR}, we sometimes take it for granted these things.*',
'*You see, {AUTHOR}, this is something you either know it or don\'t!*',
'*What are the Jews doing that we are not? You know this answer, {AUTHOR}?*',
'*Remember, {AUTHOR}, 60\% of the Jews own banks.*',
'*Remember, {AUTHOR}, 60\% of banks are owned by the Jews.*',
'*India doesn\'t have any computers. {AUTHOR}, did you know this?*',
'*{AUTHOR}, you need to reach inside and find the nugget!*',
'*You know, {AUTHOR}, a bird in the hand is WORTH IT!*',
'*They say, {AUTHOR}, what comes around GOES!*',
'*I\'m tired, {AUTHOR}, I think I might go hit my sack.*',
'*Yes, {AUTHOR}, this was the straw that broke the camel.*',
'*I\'m feeling a bit OVER the weather today, {AUTHOR}!*',
'*You are really beating around my bush, {AUTHOR}.*',
'*You know, {AUTHOR}, they say... err...*',
'*We will burn that bridge when we get there, {AUTHOR}.*',
'*You know, {AUTHOR}, a penny saved is a penny!*',
'*I believe, {AUTHOR}, that this is a blessing of the disguise!*',
'*It is as they say, {AUTHOR}, better late... yes!*',
'*Like they say, {AUTHOR}, it is water on the bridge.*',
'*Did you know that {randcomposite} is prime?*',
'*Sometimes we bark up the RIGHT tree, {AUTHOR}!*',
'*You know, {AUTHOR}, birds of a feather fly north!*',
'*Remember {AUTHOR}, actions speak loud!*',
'*I will have to take a checked rain on that one, {AUTHOR}!*'
'*Always take me with a grain of pepper, {AUTHOR}.*',
'*{AUTHOR}, we see eye to it!*',
'*I hate it when someone gives me the cold shudder, {AUTHOR}.*',
'*{AUTHOR}, have you ever tasted your own medicine?*',
'*{AUTHOR}, you are off of your ROCKS...er*',
'*You know, {AUTHOR}, you should always do unto others as you would have done unto yourself... err...*',
'*As the blacks say, the ball is in your fort {AUTHOR}!*',
'*Is there a method to your mad mess {AUTHOR}?*',
'*You know, {AUTHOR}, you can lead a horse to water, but you can\'t drink him!*',
'*{AUTHOR} You really opened my worm in the can!*',
'*{AUTHOR}, it is like the pot calling the kettle a nigger... err...*',
'*Don\'t count your chickens before they are chickens, {AUTHOR}.*',
'*It is like they say in India, you need to live and let fly, {AUTHOR}.*',
'*As John Lennon once said, {AUTHOR}, you may call me a dreamer, but I\'m not.*',
'*{AUTHOR}, please don\'t cry in the milk.*',
'*Don\'t forget, {AUTHOR}, every cloud has a silver nugget!*',
'*{AUTHOR}, it isn\'t over until my lady fat sings.*',
'*Please stop, {AUTHOR}. I have bigger fish to eat.*',
'*{AUTHOR}, my balls are in your court now.*',
'*I\'m a little hungry, {AUTHOR}. I could really go for some chips off the old block!*',
'*You know, {AUTHOR}, a picture paints a thousand pictures!*',
'*I think you are stuck between a rock and my hard place, {AUTHOR}.*',
'*Look outside, {AUTHOR}! It\'s raining cats and horses!*',
'*{AUTHOR}, an apple a day keeps my doctors at bay!*',
'*{AUTHOR}, please don\'t let the cat out of it\'s bag...*',
'*{AUTHOR}, I prefer to do things at the drop of my bhat! Get it!?*',
'*Maybe we need to address this elephant\'s room, {AUTHOR}.*',
'*Have you ever taken your caution and thrown it at the wind, {AUTHOR}?*',
'*You know, {AUTHOR}, it takes two to play the bongos!*',
'*You know, they say, {AUTHOR}, don\'t cover a book after you judge it!*',
'*This is just the calm after the storm, {AUTHOR}.*'
'*You know, {AUTHOR}, you really threw me under the boat there.*'
]

ball = [
'*I believe it is yes!*',
'*Err.. I do not believe so*',
'*I do no possess the knowledge to be the answerer*',
'*Ask again when you have TENURE... Did you know that I have TENURE??*',
'*{AUTHOR}, you are of the knowing of it!*',
'*Ask me later, {AUTHOR}...*',
'*You know... There ARE people who think yes!*',
'*{AUTHOR}, you may be doing it!*'
]

PrimeScore = {
'Dom':0,
'Etin Window':0,
'Etin Spyder':0,
'Rodger':0,
'Garry':0,
':b: :regional_indicator_r: :regional_indicator_e: :regional_indicator_a: :regional_indicator_d:':0,
':b: oston':0
}

def IsPrime(n):
    m=int(n**0.5)
    p=True
    while(m>1 and p==True):
        if(n%m==0):
            p=False
        else:
            m=m-1
    return p

@client.event
async def on_message(message):
    global PrimeScore

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Beta build only posts in beta-bhatnagar
    elif BETA == True and str(message.channel) != 'beta-bhatnagar':
        return

    # Normal build posts everywhere else
    elif BETA == False and str(message.channel) == 'beta-bhatnagar':
        return

    # This block determines nickname of AUTHOR
    if str(message.author)[:-5] in users:
        AUTHOR = users[str(message.author)[:-5]]
    else:
        AUTHOR = str(message.author)[:-5]

    if message.content.startswith('!bhat roll'):
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

    elif message.content.startswith('!bhat info'):
        MaxPlayer = max(PrimeScore, key = PrimeScore.get)
        n1 = random.randint(1, 99)
        n2 = random.randint(0, 9)
        n3 = random.randint(0, 9)
        n4 = random.randint(1, 99)
        msg = '''*Hello, {AUTHOR}! I am your tenured virtual professor, Botnagar! (ver {n1}.{n2}.{n3}:{n4})
Below is a list of commands that I may be doing them!*

    - !bhat quote *[I can tell you something juicy!]*
    - !bhat roll *[I enjoy giving out my advices for you!]*
    - !bhat prime *[I\'ll give you a prime. Let\'s see if it\'s a big one!]*
    - !bhat primescore *[Who\'s winning? Right now it\'s {MaxPlayer}!]*
    - !bhat hello *[Say hi! Don't be afraid!]*'''
        msg = msg.format(AUTHOR = AUTHOR, MaxPlayer = MaxPlayer, n1 = n1, n2 = n2, n3 = n3 , n4 =n4)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!bhat primescore'):
        MaxPlayer = max(PrimeScore, key = PrimeScore.get)
        response1 = random.choice([
        '*Here is the board of SCORES!*',
        '*Do you know.. these are all PRIMES?*',
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

    elif message.content.startswith('!bhat'):
        msg = random.choice([
        '*So... err...*',
        '*I\'m not sure I know what this is, {AUTHOR}.*'.format(AUTHOR = AUTHOR),
        '*Err... this is one of the things of which I do not know.... it!*'])
        await client.send_message(message.channel, msg)

    elif 'bhat' in message.content.lower():
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

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name = '...it!'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
