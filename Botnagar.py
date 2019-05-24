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

# Using for internet scraping
import json
import aiohttp

# Used for !bhat craps
# Still in development
import Craps

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

def gcf(x,y):
  while(y):
      x,y = y,x%y
  return x

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
        '*Try throwing your dart at this one!* https://www.amazon.com/Darts-History-Mathematics-SATISH-BHATNAGAR-ebook/dp/B0792VV5JQ/ref=sr_1_2?qid=1558167305&refinements=p_27%3ASatish++C.+Bhatnagar&s=books&sr=1-2&text=Satish++C.+Bhatnagar',
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
        '*I wrote this one many years ago!* https://www.amazon.com/PLUMS-PEACHES-EDUCATION-Satish-Bhatnagar/dp/1490770712',
        '*Have a look at my Mama Ji!* https://www.amazon.com/Swami-Deekshanand-Saraswati-My-Mama-ebook/dp/B0792XXDLM/ref=sr_1_1?qid=1558167305&refinements=p_27%3ASatish++C.+Bhatnagar&s=books&sr=1-1&text=Satish++C.+Bhatnagar',
        '*Matherticles! Yes!* https://www.amazon.com/Converging-Matherticles-Mathematical-Reflections-II/dp/1490757309/ref=sr_1_5?qid=1558167305&refinements=p_27%3ASatish++C.+Bhatnagar&s=books&sr=1-5&text=Satish++C.+Bhatnagar',
        '*You know, epsilons and deltas aren\'t just used for calculus... err...* https://www.amazon.com/Epsilons-Deltas-Life-Everyday-Stories-ebook/dp/B07957WRZ3/ref=sr_1_6?qid=1558167305&refinements=p_27%3ASatish++C.+Bhatnagar&s=books&sr=1-6&text=Satish++C.+Bhatnagar',
        '*They say education is like a rare fruit...* https://www.amazon.com/Plums-Peaches-Pears-Education-I-ebook/dp/B0793TH8MY/ref=sr_1_7?qid=1558167305&refinements=p_27%3ASatish++C.+Bhatnagar&s=books&sr=1-7&text=Satish++C.+Bhatnagar',
        '*You may be reading up on my religion!* https://www.amazon.com/My-Hindu-Faith-Periscope-I-ebook/dp/B0792X25DY/ref=sr_1_8?qid=1558167305&refinements=p_27%3ASatish++C.+Bhatnagar&s=books&sr=1-8&text=Satish++C.+Bhatnagar',
        '*This is a good book on where I am from! Yes!* https://www.amazon.com/Via-Bhatinda-Braid-Reflected-Memoirs/dp/1466984678/ref=sr_1_3?qid=1558167305&refinements=p_27%3ASatish++C.+Bhatnagar&s=books&sr=1-3&text=Satish++C.+Bhatnagar',
        '*You know, there are many DARTS in my book, yes!*',
        '*Have you BHAT my book yet, {AUTHOR}??*'.format(AUTHOR = AUTHOR)
        ])
        await client.send_message(message.channel, msg)

    # standard build only posts in bhatnagar
    elif str(message.channel) != 'botnagar' and str(message.channel) != 'botnagar-workshop':
        return

    # Bhat tells us the price of ethereum
    elif message.content.startswith('!bhat ethprice'):
        file = open('EthereumAPI.dat', 'r')
        KEY = file.read()
        file.close()
        url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH&tsyms=USD&api_key=' + KEY
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            msg = random.choice([
            '*I do believe the Ethereum is at ${PRICE}!*',
            '*Err, Ethereum might be at ${PRICE}....*',
            '*Did you know that ${PRICE} is the value of the Ethereums??*',
            '*You know, some say that ${PRICE} is what Ethereum is at yes!*'
            ])
            await client.send_message(message.channel, msg.format(PRICE = str(response['ETH']['USD'])))

    # Bhat 8ball roller
    elif message.content.startswith('!bhat 8ball'):
        msg = random.choice(ball).format(AUTHOR = AUTHOR)
        await client.send_message(message.channel, msg)

    # Add quotes to Bhat's list
    elif message.content.startswith('!bhat addquote'):
        s = str(message.content)[15:]
        if s[0] != '*':
            s = '*' + s
        if s[-1] != '*':
            s = s + '*'
        quotesFile = open('Quotes.dat', 'a')
        quotesFile.write('\n' + s)
        quotesFile.close()
        msg = random.choice([
        '*You know, I have placed it in my MIND!*',
        '*I will be of the thinking it!*',
        '*Err, I will memory this one, yes!*'
        ])
        await client.send_message(message.channel, msg)

    # New Bhat random quote
    elif message.content.startswith('!bhat quote'):
        randcomposite = random.randint(3, 100)
        while IsPrime(randcomposite):
            randcomposite = random.randint(3, 100)
        quotesFile = open('Quotes.dat', 'r')
        s = quotesFile.read()
        quotesFile.close()
        quotesList = s.split('\n')
        msg = random.choice(quotesList).format(AUTHOR = AUTHOR, randcomposite = randcomposite)
        await client.send_message(message.channel, msg)

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
        '\n    - !bhat bday *[How old am I? I\'ll give you my birth year!]*'
        '\n    - !bhat roll *[Roll some number cubes! How fun!]*'
        '\n    - !bhat ethprice *[You know, Ethereum has a price!]*'
        '\n    - !bhat krypto *[Maybe you can\'t solve this one? Give me 6 numbers like this n1, n2, n3, n4, n5, target]*'
        '\n    - !bhat factor *[I can simplify... err... some trinomials. Give me a, b, and c!]*'
        '\n    - !bhat cards *[Tell me how many playing cards you want. I will give them to you at random!]*'
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

    # Bhat trinomial factoring
    elif message.content.startswith('!bhat factor'):

        l = str(message.content).split()
        [a, b, c] = l[2].split(',')
        a = int(a)
        b = int(b)
        c = int(c)

        bhatknows = True
        factorable = False

        if(a%1!=0 or b%1!=0 or c%1!=0 or a<0 or b<0 or c<0):
            msg = random.choice([
            '*These are not nonnegative integers!*',
            '*Do you not know what the whole numbers are?*',
            '*You know, these numbers are difficult to work with... err...*',
            '*Try some other numbers! Yes!*'
            ])
        else:
            if(a==0 and b==0 and c==0):
                trinomial = '0'
                factorable = False

            if(a==0 and b==0 and c!=0):
                trinomial = str(c)
                factorable = False

            if(a==0 and b!=0 and c==0):
                if(b==1):
                    trinomial = 'x'
                else:
                    trinomial = str(b)+'x'
                factorable = False

            if(a!=0 and b==0 and c==0):
                if(a==1):
                    trinomial = 'x'+chr(178)
                else:
                    trinomial = str(a)+'x'+chr(178)
                factorable = False

            if(a==0 and b!=0 and c!=0):
                if(b==1):
                    trinomial = 'x+'+str(c)
                    factorable = False
                else:
                    trinomial = str(b)+'x+'+str(c)
                    if(gcf(b,c)==1):
                        factorable = False
                    else:
                        factorable = True
                        if(b/gcf(b,c)==1):
                            solution = str(gcf(b,c))+'(x+'+str(c//gcf(b,c))+')'
                        else:
                            solution = str(gcf(b,c))+'('+str(b//gcf(b,c))+'x+'+str(c//gcf(b,c))+')'

            if(a!=0 and b!=0 and c==0):
                if(a==1):
                    if(b==1):
                        trinomial = 'x'+chr(178)+'+x'
                    else:
                        trinomial = 'x'+chr(178)+'+'+str(b)+'x'
                else:
                    if(b==1):
                        trinomial = str(a)+'x'+chr(178)+'+x'
                    else:
                        trinomial = str(a)+'x'+chr(178)+'+'+str(b)+'x'
                factorable = True
                if(gcf(a,b)==1):
                    if(a==1):
                        solution = 'x(x+'+str(b)+')'
                    else:
                        solution = 'x('+str(a)+'x+'+str(b)+')'
                else:
                    if(a/gcf(a,b)==1):
                        solution = str(gcf(a,b))+'x(x+'+str(b//gcf(a,b))+')'
                    else:
                        solution = str(gcf(a,b))+'x('+str(a//gcf(a,b))+'x+'+str(b//gcf(a,b))+')'

            if(a!=0 and b==0 and c!=0):
                if(a==1):
                    trinomial = 'x'+chr(178)+'+'+str(c)
                else:
                    trinomial = str(a)+'x'+chr(178)+'+'+str(c)
                if(gcf(a,c)==1):
                    factorable = False
                else:
                    factorable = True
                    if(a/gcf(a,c)==1):
                        solution = str(gcf(a,c))+'(x'+chr(178)+'+'+str(c//gcf(a,c))+')'
                    else:
                        solution = str(gcf(a,c))+'('+str(a//gcf(a,c))+'x'+chr(178)+'+'+str(c//gcf(a,c))+')'

            if(a!=0 and b!=0 and c!=0):
                if(a==1):
                    if(b==1):
                        trinomial = 'x'+chr(178)+'+x+'+str(c)
                    else:
                        trinomial = 'x'+chr(178)+'+'+str(b)+'x+'+str(c)
                else:
                    if(b==1):
                        trinomial = str(a)+'x'+chr(178)+'+x+'+str(c)
                    else:
                        trinomial = str(a)+'x'+chr(178)+'+'+str(b)+'x+'+str(c)
                if(gcf(gcf(a,b),c)==1):
                    if(a==1):
                        if(((-b+(b**2-4*a*c)**(1/2))/(2*a))%1==0):
                            factorable = True
                            x = -(-b-(b**2-4*a*c)**(1/2))//(2*a)
                            y = -(-b+(b**2-4*a*c)**(1/2))//(2*a)
                            solution = '(x+'+str(x)+')(x+'+str(y)+')'
                        else:
                            factorable = False
                    else:
                        if(((-b+(b**2-4*a*c)**(1/2))//(2*a))%1==0):
                            bhatknows = False
                        else:
                            factorable = False
                            bhatknows = False
                else:
                    bhatknows = False

            if(bhatknows == True):
                if(factorable == True):
                    msg = '*The polynomial '+trinomial+' factors into '+solution+'!*'
                else:
                    msg = '*The polynomial '+trinomial+' doesn\'t factor!*'
            else:
                #msg = '*This is... err... something that I haven\'t learned yet...*\n=pup factor {a}x^2+{b}x+{c}'.format(a = a, b = b, c = c)
                msg = '=pup factor {a}x^2+{b}x+{c}'.format(a = a, b = b, c = c)
        await client.send_message(message.channel, msg)

    # Bhat's birth year
    elif message.content.startswith('!bhat bday'):
        if(random.random()<.05):
            century = 17
        elif(random.random()<.05):
            century = 20
        elif(random.random()<.20):
            century = 18
        else:
            century = 19
        if(century==20):
            year = int((100*random.random())/5)
        else:
            year = int((100*random.random()))
        if(year < 10):
            bday = str(century)+str(0)+str(year)
        else:
            bday = str(century)+str(year)
        msg = random.choice([
        '*Did you know that I was born in the year of '+bday+'?*',
        '*Yes, this does remind me of my time back in '+bday+'!*',
        '*You know, when I was a little girl in '+bday+'... err...*',
        '*I was born in '+bday+'! What a wonderful year this is!*'
        ])
        if IsPrime(year):
            msg = msg + '\n*...And did you know that '+bday+' is :b:rime??*'
        await client.send_message(message.channel, msg)

    # Bhat random cards

    elif message.content.startswith('!bhat cards'):
        string = str(message.content)
        n = int(string.[2])

        def SelectCards(n, cards):
            deck = ("AS","2S","3S","4S","5S","6S","7S","8S","9S","XS","JS","QS","KS",
                    "AH","2H","3H","4H","5H","6H","7H","8H","9H","XH","JH","QH","KH",
                    "AD","2D","3D","4D","5D","6D","7D","8D","9D","XD","JD","QD","KD",
                    "AC","2C","3C","4C","5C","6C","7C","8C","9C","XC","JC","QC","KC")
            i = 0
            while(i < n):
                new = False
                while(new == False):
                    candidate = random.choice(deck)
                    if(candidate not in cards):
                        new = True
                cards.append(candidate)
                i = i+1

        def IsTen(card):
            if(card[0] == "X"):
                return True
            else:
                return False

        def PrintCards(n, cards):

            line1 = "```"
            i = 0
            while(i < n):
                line1 = line1+chr(9556)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9559)+" "
                i = i + 1

            line2 = str()
            i = 0
            while(i < n):
                line2 = line2+chr(9553)
                if(IsTen(cards[i][0])):
                    line2 = line2+"10"
                else:
                    line2 = line2+" "+cards[i][0]
                line2 = line2+"   "+chr(9553)+" "
                i = i + 1

            line3 = str()
            i = 0
            while(i < n):
                line3 = line3+chr(9553)+"  "
                if(cards[i][1] == "S"):
                    line3 = line3+chr(9824)
                elif(cards[i][1] == "H"):
                    line3 = line3+chr(9829)
                elif(cards[i][1] == "D"):
                    line3 = line3+chr(9830)
                else:
                    line3 = line3+chr(9827)
                line3 = line3+"  "+chr(9553)+" "
                i = i + 1

            line4 = str()
            i = 0
            while(i < n):
                line4 = line4+chr(9553)+"   "
                if(IsTen(cards[i][0])):
                    line4 = line4+"10"
                else:
                    line4 = line4+cards[i][0]+" "
                line4 = line4+chr(9553)+" "
                i = i + 1

            line5 = str()
            i = 0
            while(i < n):
                line5 = line5+chr(9562)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9565)+" "
                i = i + 1
            line5 = line5+"```"

            msg = line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5
            await client.send_message(message.channel, msg)

        if(n > 10):
            msg = "*This is just too many of the cards!*"
            await client.send_message(message.channel, msg)
        else:
            cards = list()
            SelectCards(n, cards)
            PrintCards(n, cards)

    # Wrong command check
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
