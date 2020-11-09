from utils import player

class Board:
    """
    Class that create a game board with the list of players, a turn count, the cards that were played this turn and
    all the card that were played during the game.
    """
    def __init__(self):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_card = []

    def start_game(self):
        """
        Start the game using all classes and methods defined in the others files.
        """
        print("The game starts !")
        # Loop to enter all the players'name.
        while True:
            player_name = input("Enter a player name or 'end' if you entered all of them:")
            if player_name == "end":
                break
            else:
                self.players += [player.Player(player_name)]
                print("{} added to the players!".format(player_name))
        # Create an object deck
        main_deck = player.Deck()
        # Create the cards in the deck.
        main_deck.fill_deck()
        # Shuffles all the cards.
        main_deck.shuffle()
        # Distribute all the cards to the players.
        main_deck.distribute(self.players)
        # Each turn of the loop is one turn of the game.
        for i in range(0, int(52 / len(self.players))):
            self.active_cards = []
            for j in self.players:
                card = j.play()
                self.active_cards += [card]
                j.cards.remove(card)
                j.turn_count += 1
            self.history_card += self.active_cards
            self.turn_count += 1
            print("turn nbr : {} \nCards played this turn : {}\nNumber of cards played in the game : {}".format(
                self.turn_count, self.active_cards, len(self.history_card)
            ))
        print("You have no cards left, it's the end !")

    def __str__(self):
        return "This is a board."
