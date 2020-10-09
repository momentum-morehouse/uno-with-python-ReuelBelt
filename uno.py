from random import randint

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔴","🟢","🟡","🔵" ]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __str__(self):
        return f"{self.number} {self.color}"   


class Player:
    def __init__(self, name):
        self.name = name 
        #list of 7 cards
        self.hand = []


class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = Card(color, number)
                self.cards.append(card)

    def shuffle(self):
        random_deck = []
            #get access to the cards
        deck_copy = self.cards.copy()
            #choose a random card in that deck
        while len(deck_copy) > 0: 
            random_card = deck_copy[randint(0, len(deck_copy)-1)]
            #take that card and put it into the random deck 
            random_deck.append(random_card)  
            #remove that card from the original deck 
            deck_copy.remove(random_card)

        return random_deck
        

class Game:
    def __init__(self):
    #get each player's name from input
        player_1_name = input("Player 1 what is your name ")
        player_2_name = input("Player 2 what is your name ")
    #players 2 (up to 10 is allowed)
    #2 instances of players
        self.player_1 = Player(player_1_name)
        self.player_2 = Player(player_2_name)
    #make a deck
    #shuffle deck
        self.deck = Deck(NUMBERS, COLORS).shuffle()
    
        self.winner = False 
        #while self.winner = false keep doing this
        #until something in game play happens to change this 
        #switch game on and off 

        self.deal()
    
        print(len(self.player_1.hand), len(self.player_2.hand))

    def deal(self):
    #determine order of dealing
        #how to do pop with an index 
        #while length of 
    #deal cards alternate between each players until both have 7
    #use loop to deal cards, multiple rounds (round 1, etc.)
    #take a card from the top of shuffled deck and append card to each players hand for 7 rounds
        while len(self.player_2.hand) < 7:
            card_1 = self.deck.pop()
            self.player_1.hand.append(card_1)
            card_2 = self.deck.pop()
            self.player_2.hand.append(card_2)
    
    def turn(self, player):
        pass
        #would sync with game turn

game = Game()
for card in game.deck:
    print(str(card))

print(f"{game.player_1.name}'s hand")

for card in game.player_1.hand:
    print(card)

print(f"{game.player_2.name}'s hand")
for card in game.player_2.hand: 
    print(card)

game.turn(game.player_1)
#write some loop
#what one player's indivdual look like
#what cards pop removed or appended to
#sometimes good to store boolean on player (i.e. still playing)