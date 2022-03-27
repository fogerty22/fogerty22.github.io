import random
MAX = 21

class Player:
    def __init__(self, n, hv):
        self.name = n
        self.handValue = hv
    
    def __str__(self):
        return("Your hand value is: ", self.handValue) # I want this to print with each turn
    
    def update_hand_value(self, card):
        return(self.name +"\t"+ " was dealt " + str(card))
    
    def displayHand(self):
        return(self.name+"\t"+"'s hand value is "+self.hv)


def main():
    instructions()

    handValue1 = 0
    handValue2 = 0
    player1 = Player(input("What is your name, Player 1? "), handValue1)
    player2 = Player(input("What is your name, Player 2? "), handValue2)
    deck = create_deck()

    card1 = deal(deck)
    card2 = deal(deck)
    
    player1.update_hand_value(card1)
    player2.update_hand_value(card2)

    handValue1 = card1
    handValue2 = card2

    print(player1.name, " is dealt ", handValue1)
    print(player2.name, " is dealt ", handValue2)

    if card1 == 1:
        handValue1 = 1
    elif card1 == 2:
        handValue1 = 2
    elif card1 == 3:
        handValue1 = 3
    elif card1 == 4:
        handValue1 = 4
    elif card1 == 5:
        handValue1 = 5
    elif card1 == 6:
        handValue1 = 6
    elif card1 == 7:
        handValue1 = 7
    elif card1 == 8:
        handValue1 = 8
    elif card1 == 9:
        handValue1 = 9
    elif card1 == 10:
        handValue1 = 10
    else:
        handValue1 = 10
    #handValue1 = (value)

    if card2 == 1:
        handValue2 = 1
    elif card2 == 2:
        handValue2 = 2
    elif card2 == 3:
        handValue2 = 3
    elif card2 == 4:
        handValue2 = 4
    elif card2 == 5:
        handValue2 = 5
    elif card2 == 6:
        handValue2 = 6
    elif card2 == 7:
        handValue2 = 7
    elif card2 == 8:
        handValue2 = 8
    elif card2 == 9:
        handValue2 = 9
    elif card2 == 10:
        handValue2 = 10
    else:
        handValue2 = 10
    #handValue1 = (value)

    hitOrStay(player1, player2, deck, handValue1, handValue2)


def instructions():
    input("Welcome! Press enter to navigate the program. ")
    input("This program is a 2-player game of Blackjack. ")
    input("Blackjack is a card game where players compete against the card dealer, " +
        "as well as each other. ")
    input("With this, each player will have a pre-determined deck from the dealer. ")
    input("Each card in the deck has a value between 1-10. ")
    input("The player with the highest sum of cards, while less than or equal to 21, wins. ")
    input("The player with a hand value greater than 21 loses. ")
    input("Tie games are allowed. ")
    input("This game will have two players. Player 1 will go first at each turn. ")


def create_deck():
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    deck = {}
    for suit in suits:
        for num in numbers:
            if num.isnumeric(): 
                deck[num + ' of ' + suit] = int(num)
            else: 
                deck[num + ' of ' + suit] = special_values[num]

    return deck



def deal(deck):

    keys = list(deck.keys())
    random.shuffle(keys)
    value = deck.pop(keys[0])
    return(value)


def hitOrStay(player1, player2, deck, handValue1, handValue2):
    gameOver = False
    #new_handValue1 = 0
    print(player1.name + ": ")
    print("Your current hand value is: ", handValue1)
    ask_newcard1 = input("Hit or stay? [Hit/Stay]: ")
    if handValue1 < MAX and gameOver != True and ask_newcard1 == "Hit":
        deal2(player1, handValue1)
        #print("Your updated hand value is: ", new_handValue1)
    else:
        gameOver = True
        print("Game over, " + player1.name + " !")
        handValue1 = 22
    # new_handValue2 = 0
    print(player2.name + ": ")
    print("Your current hand value is: ", handValue2)
    ask_newcard2 = input("Hit or stay? [Hit/Stay]: ")
    if handValue2 < MAX and gameOver != True and ask_newcard2 == "Hit":
        deal3(player1, player2, handValue1, handValue2, gameOver)
        #print("Your updated hand value is: ", new_handValue2)
    else:
        gameOver = True
        print("Game over, " + player2.name + "!")
        handValue2 = 22


def deal2(player1, handValue1):
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    deck = {}
    for suit in suits:
        for num in numbers:
            if num.isnumeric(): 
                deck[num + ' of ' + suit] = int(num)
            else: 
                deck[num + ' of ' + suit] = special_values[num]
    
    keys = list(deck.keys())
    random.shuffle(keys)
    value = deck.pop(keys[0])


    if value == 1:
        temp_handValue1 = 1
    elif value == 2:
        temp_handValue1 = 2
    elif value == 3:
        temp_handValue1 = 3
    elif value == 4:
        temp_handValue1 = 4
    elif value == 5:
        temp_handValue1 = 5
    elif value == 6:
        temp_handValue1 = 6
    elif value == 7:
        temp_handValue1 = 7
    elif value == 8:
        temp_handValue1 = 8
    elif value == 9:
        temp_handValue1 = 9
    elif value == 10:
        temp_handValue1 = 10
    else:
        temp_handValue1 = 10
    #handValue1 = (value)
    player1.update_hand_value(card=value)
    new_handValue1 = handValue1 + temp_handValue1
    print("Your updated hand value is: ", new_handValue1)

def deal3(player1, player2, handValue1, handValue2, gameOver):
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    deck = {}
    for suit in suits:
        for num in numbers:
            if num.isnumeric(): 
                deck[num + ' of ' + suit] = int(num)
            else: 
                deck[num + ' of ' + suit] = special_values[num]
    
    keys = list(deck.keys())
    random.shuffle(keys)
    value = deck.pop(keys[0])


    if value == 1:
        temp_handValue2 = 1
    elif value == 2:
        temp_handValue2 = 2
    elif value == 3:
        temp_handValue2 = 3
    elif value == 4:
        temp_handValue2 = 4
    elif value == 5:
        temp_handValue2 = 5
    elif value == 6:
        temp_handValue2 = 6
    elif value == 7:
        temp_handValue2 = 7
    elif value == 8:
        temp_handValue2 = 8
    elif value == 9:
        temp_handValue2 = 9
    elif value == 10:
        temp_handValue2 = 10
    else:
        temp_handValue2 = 10
    #handValue1 = (value)
    player2.update_hand_value(card=value)
    new_handValue2 = handValue2 + temp_handValue2
    print("Your updated hand value is: ", new_handValue2)

    isAWinner(player1, player2, handValue1, handValue2, gameOver)
    

def isAWinner(player1, player2, hand1, hand2, gameOver):
    if hand1 > hand2 and gameOver != True:
        print("Congratulations, " + player1.name + ", you win the game! ")
    elif hand1 < hand2 and gameOver != True:
        print("Congratulations, " + player1.name + ", you win the game! ")
    else:
        print("It is a draw-- there is no winner. ")

main()