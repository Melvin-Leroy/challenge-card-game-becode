from utils import card
from random import shuffle
from random import randint

class Player:
    """
    Class that create a player with his name, his hand, his turn count, his number of cards and his history.
    """
    def __init__(self,name: str):
        """
        Initialize a player.

        :param name: Give a name to the player.
        """
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play(self):
        """
        Take a card from the player's hand and play it on the board

        :return: The card he plays.
        """
        card = self.cards[randint(0, len(self.cards))]
        self.history += [card]
        print(self.name, self.turn_count, "played:", card.value, card.icon)
        return card

class Deck:
    """
    Class that create a deck of cards in a list.
    """
    def __init__(self):
        """
        Initialize the deck with a blank list.
        """
        self.cards = []

    def fill_deck(self):
        """
        Fill in the deck with the 52 classical cards of deck of cards.
        """
        for i in ["♥", "♦", "♣", "♠"]:
            for j in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                deck_card = card.Card(j, i)
                self.cards += [deck_card]

    def shuffle(self):
        """
        Shuffle the deck of cards.
        """
        shuffle(self.cards)

    def distribute(self, list_of_players : list):
        """
        Distribute the deck's cards in players' hands.

        :param list_of_players: The list of players in the game.
        """
        number_of_cards = int(52 / len(list_of_players))
        for i in list_of_players:
            for j in range(0, number_of_cards):
                i.cards += [self.cards[0]]
                self.cards.remove(self.cards[0])

    def __str__(self):
        return "This is a deck of cards."