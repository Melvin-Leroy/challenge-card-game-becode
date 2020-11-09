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
        print(self.name, self.turn_count, "played:", card.value, card.icon)
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

    def distribute(self, list_of_players):
        number_of_cards = int(52 / len(list_of_players))
        for i in list_of_players:
            for j in range(0, number_of_cards):
                i.cards += [self.cards[0]]
                self.cards.remove(self.cards[0])




    def __str__(self):
        return "This is a deck of cards."