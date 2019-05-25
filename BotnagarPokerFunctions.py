import random

def Select5Cards(cards): #selects five random cards

    deck = ("AS","2S","3S","4S","5S","6S","7S","8S","9S","XS","JS","QS","KS",
            "AH","2H","3H","4H","5H","6H","7H","8H","9H","XH","JH","QH","KH",
            "AD","2D","3D","4D","5D","6D","7D","8D","9D","XD","JD","QD","KD",
            "AC","2C","3C","4C","5C","6C","7C","8C","9C","XC","JC","QC","KC")
    i = 0
    while(i < 5):
        new = False
        while(new == False):
            candidate = random.choice(deck)
            if(candidate not in cards):
                new = True
        cards.append(candidate)
        i = i+1

def IsTen(card): #checks to see if a card's rank is 10
    if(card[0] == "X"):
        return True
    else:
        return False

def Print5Cards(cards): #prints the five random cards

    line1 = "```"
    i = 0
    while(i < 5):
        line1 = line1+chr(9556)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9559)+" "
        i = i + 1

    line2 = str()
    i = 0
    while(i < 5):
        line2 = line2+chr(9553)
        if(IsTen(cards[i][0])):
            line2 = line2+"10"
        else:
            line2 = line2+" "+cards[i][0]
        line2 = line2+"   "+chr(9553)+" "
        i = i + 1

    line3 = str()
    i = 0
    while(i < 5):
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
    while(i < 5):
        line4 = line4+chr(9553)+"   "
        if(IsTen(cards[i][0])):
            line4 = line4+"10"
        else:
            line4 = line4+cards[i][0]+" "
        line4 = line4+chr(9553)+" "
        i = i + 1

    line5 = str()
    i = 0
    while(i < 5):
        line5 = line5+chr(9562)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9552)+chr(9565)+" "
        i = i + 1
    line5 = line5+"```"

    return line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"

def IsFlush(cards): #checks to see if hand is a flush
    i = 0
    while(i < 4):
        if(cards[i][1] != cards[i+1][1]):
            return False
        i = i + 1
    return True

def ConvertFace(rank): #converts card ranks into numbers for easy ordering
    if(rank == "A"):
        return 1
    elif(rank == "X"):
        return 10
    elif(rank == "J"):
        return 11
    elif(rank == "Q"):
        return 12
    elif(rank == "K"):
        return 13
    else:
        return int(rank)

def ConvertFaceAlt(rank): #alternate numbering for determining highest card
    if(rank == "X"):
        return 10
    elif(rank == "J"):
        return 11
    elif(rank == "Q"):
        return 12
    elif(rank == "K"):
        return 13
    elif(rank == "A"):
        return 14
    else:
        return int(rank)

def SortCards(cards): #orders cards by ascending rank
    card1 = ConvertFace(cards[0][0])
    card2 = ConvertFace(cards[1][0])
    card3 = ConvertFace(cards[2][0])
    card4 = ConvertFace(cards[3][0])
    card5 = ConvertFace(cards[4][0])
    ranks = [card1, card2, card3, card4, card5]
    ranks.sort()
    return ranks

def IsStraight(cards): #checks to see if hand is a straight
    ranks = SortCards(cards)
    if(ranks[0] == 1 and ranks[1] == 10 and ranks[2] == 11 and ranks[3] == 12 and ranks[4] == 13):
        return "Royal"
    else:
        i = 0
        while(i < 4):
            if(ranks[i]+1 != ranks[i+1]):
                return "NoStraight"
            i = i + 1
        return "Straight"

def IsFour(cards): #checks to see if hand has four of a kind
    ranks = SortCards(cards)
    if(ranks[0] == ranks[1] and ranks[1] == ranks[2] and ranks[2] == ranks[3]):
        return True
    elif(ranks[1] == ranks[2] and ranks[2] == ranks[3] and ranks[3] == ranks[4]):
        return True
    else:
        return False

def IsThree(cards): #checks to see if hand has three of a kind
    ranks = SortCards(cards)
    if(ranks[0] == ranks[1] and ranks[1] == ranks[2]):
        return True
    elif(ranks[1] == ranks[2] and ranks[2] == ranks[3]):
        return True
    elif(ranks[2] == ranks[3] and ranks[3] == ranks[4]):
        return True
    else:
        return False

def IsFull(cards): #checks to see if hand is a full house
    ranks = SortCards(cards)
    if(ranks[0] == ranks[1] and ranks[3] == ranks[4]):
        return True
    else:
        return False

def Is2Pairs(cards): #checks to see if hand has two pairs
    ranks = SortCards(cards)
    if(ranks[0] == ranks[1] and ranks[2] == ranks[3]):
        return True
    elif(ranks[0] == ranks[1] and ranks[3] == ranks[4]):
        return True
    elif(ranks[1] == ranks[2] and ranks[3] == ranks[4]):
        return True
    else:
        return False

def IsPair(cards): #checks to see if hand has a pair
    ranks = SortCards(cards)
    if(ranks[0] == ranks[1] or ranks[1] == ranks[2] or ranks[2] == ranks[3] or ranks[3] == ranks[4]):
        return True
    else:
        return False

def HighCard(cards): #checks for highest card and grabs card info
    highest = 0
    highcard = str()
    i = 0
    while(i < 5):
        if(cards[i][1] == "S"):
            n = 3
        elif(cards[i][1] == "H"):
            n = 2
        elif(cards[i][1] == "D"):
            n = 1
        else:
            n = 0
        candidate = ConvertFaceAlt(cards[i][0])*10 + n
        if(candidate > highest):
            highest = candidate
            highcard = cards[i]
        i = i + 1
    return highcard

def FormatRank(card): #formats the rank of the highest card
    if(card[0] == "A"):
        return "Ace"
    elif(card[0] == "2"):
        return "two"
    elif(card[0] == "3"):
        return "three"
    elif(card[0] == "4"):
        return "four"
    elif(card[0] == "5"):
        return "five"
    elif(card[0] == "6"):
        return "six"
    elif(card[0] == "7"):
        return "seven"
    elif(card[0] == "8"):
        return "eight"
    elif(card[0] == "9"):
        return "nine"
    elif(card[0] == "X"):
        return "ten"
    elif(card[0] == "J"):
        return "Jack"
    elif(card[0] == "Q"):
        return "Queen"
    else:
        return "King"

def FormatSuit(card): #formats the suit of the highest card
    if(card[1] == "S"):
        return "spades"
    elif(card[1] == "H"):
        return "hearts"
    elif(card[1] == "D"):
        return "diamonds"
    else:
        return "clubs"

def Test5Cards(cards): #checks for hand and returns rank

    if(IsFlush(cards) == True and IsStraight(cards) == "Royal"):
        return "a Royal Flush"

    elif(IsFlush(cards) == True and IsStraight(cards) == "Straight"):
        return "a Straight Flush"

    elif(IsFour(cards) == True):
        return "Four of a Kind"

    elif(IsThree(cards) == True and IsFull(cards) == True):
        return "a Full House"

    elif(IsFlush(cards) == True):
        return "a Flush"

    elif(IsStraight(cards) == "Royal" or IsStraight(cards) == "Straight"):
        return "a Straight"

    elif(IsThree(cards) == True):
        return "Three of a Kind"

    elif(Is2Pairs(cards) == True):
        return "Two Pairs"

    elif(IsPair(cards) == True):
        return "a Pair"

    else:
        return HighCard(cards)
