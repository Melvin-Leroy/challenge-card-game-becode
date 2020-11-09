from utils import card
from random import shuffle
from random import randint

class Player:
    def __init__(self,name: str):
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play(self):
        card = self.cards[randint(0, len(self.cards))]
        self.history += [card]
        print(self.name, self.turn_count, "played:", card.value, card.symbol)
        return card

class Deck:
    def __init__(self):
        self.cards = []

    def fill_deck(self):
        for i in ["♥", "♦", "♣", "♠"]:
            for j in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                deck_card = card.Card(j, i)
                self.cards += [deck_card]

    def shuffle(self):
        shuffle(self.cards)

    #def distribute(self):
        #for i in players:




test_deck = Deck()
print(test_deck.cards)

test_deck.fill_deck()
print(len(test_deck.cards))
print(test_deck.cards)

test_deck.shuffle()
print(test_deck.cards)