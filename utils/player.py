import Card from card.py

class Player:
    def __init__(self,name: str):
        self.name = name
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play(self):
        #pick a card in self.cards
        self.history += [card]
        print(self.name, self.turn_count, "played:", card.value, card.symbol)
        return card