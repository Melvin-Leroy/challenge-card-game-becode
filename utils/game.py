from utils import player

class Board:
    def __init__(self):
        self.players = []
        self.turn_count = 0
        self.active_cards = []
        self.history_card = []

    def start_game(self):
        print("The game starts !")
        while True:
            player_name = input("Enter a player name or 'end' if you entered all of them:")
            if player_name == "end":
                break
            else:
                self.players += [player.Player(player_name)]
                print("{} added to the players!".format(player_name))
        main_deck = player.Deck()
        main_deck.fill_deck()
        main_deck.shuffle()
        main_deck.distribute(self.players)
        for i in range(0, int(52 / len(self.players))):
            self.active_cards = []
            for j in self.players:
                self.active_cards += [j.play()]
                j.turn_count += 1
            self.history_card += self.active_cards
            self.turn_count += 1
            print("turn nbr : {} \nCards played this turn : {}\nNumber of cards played in the game : {}".format(
                self.turn_count, self.active_cards, len(self.history_card)
            ))




    def __str__(self):
        return "This is a board."
