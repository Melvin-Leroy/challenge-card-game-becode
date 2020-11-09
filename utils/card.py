
class Symbol:
    def __init__(self, icon: str):
        self.icon = icon
        if icon == "♥" or icon == "♦":
            self.color = "red"
        else :
            self.color = "black"

    def __str__(self):
        return "A {} card with the color {}".format(self.icon, self.color)

class Card(Symbol):
    def __init__(self, value: str, icon: str):
        super().__init__(icon)
        self.value = value

    def __str__(self):
        return "The {} of {}".format(self.value, self.icon)
