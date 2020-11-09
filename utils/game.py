from utils import player
from heapq import nlargest


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
            cards = []
            # The player sees his cards and decide which he wants to play.
            for j in self.players:
                print("{}, your turn!".format(j.name))
                for k in range(len(j.cards)):
                    print("{}) {}".format(k, j.cards[k]))
                card = j.play()
                cards += [card]
                self.active_cards += [card]
                j.cards.remove(card)
                j.turn_count += 1
            # change the values of non digital cards.
            values = []
            for k in cards:
                if k.value == "A" or "J" or "Q" or "K":
                    if k.value == "A":
                        values += [1]
                    elif k.value == "J":
                        values += [11]
                    elif k.value == "Q":
                        values += [12]
                    elif k.value == "K":
                        values += [13]
                    else:
                        values += [int(k.value)]
            # #Identify the greatest value(s).
            max_value = max(values)
            index = [index for index, value in enumerate(values) if value == max_value]
            # Give players points if they have the best cards.
            for l in index:
                self.players[l].points += 1
            for m in self.players:
                print("{} has {} points.".format(m.name, m.points))
            # Some information about the round
            self.history_card += self.active_cards
            self.turn_count += 1
            print("turn nbr : {} \nNumber of cards played in the game : {}".format(self.turn_count, len(self.history_card)))
            print("cards played this round :", *self.active_cards, sep = "\n")
            # If the actual winner have to much point compares to others, the game stops.
            winner_points = []
            for p in self.players:
                winner_points += [p.points]
            two_bests = nlargest(2, winner_points)
            if max(two_bests) - min(two_bests) >= int(52 / len(self.players)) - self.turn_count:
                break
        print("You have no cards left or the winner is too much ahead, it's the end !")
        # Show who has the grater amount of points, the winner(s).
        winner_values = []
        for n in self.players:
            winner_values += [n.points]
        max_winner_value = max(winner_values)
        winner_index = [index for index, value in enumerate(winner_values) if value == max_winner_value]
        for o in winner_index:
            print("{} is a winner!".format(self.players[o].name))

    def __str__(self):
        return "players : {}, turn : {}, cards played this turn : {}, cards played : {}".format(
            self.players, self.turn_count, self.active_cards, self.history_card
        )
