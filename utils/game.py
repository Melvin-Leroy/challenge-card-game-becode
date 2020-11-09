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
        main_deck = player.Deck()
        main_deck.fill_deck()
        print(main_deck.cards)
        main_deck.shuffle()
        print(main_deck.cards)
        main_deck.distribute(self.players)
        for i in self.players:
            i.play()
            self.active_cards += [i.play()]




    def __str__(self):
        return "This is a board."
