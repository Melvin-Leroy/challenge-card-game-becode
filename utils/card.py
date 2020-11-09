
class Symbol:
    """
    Class that create a symbol and a color for a card.
    """
    def __init__(self, icon: str):
        """
        Initialize a Symbol object with an icon and a color.

        :param icon: A string in ["♥", "♦", "♣", "♠"] that gives the symbol.
        :color: The color is automatically retrieved from the symbol.
        """
        self.icon = icon
        if icon == "♥" or icon == "♦":
            self.color = "red"
        else :
            self.color = "black"

    def __str__(self):
        return "icon : {}, color : {}".format(self.icon, self.color)

class Card(Symbol):
    """
    Class that create a card based on its parent class Symbol.
    """
    def __init__(self, value: str, icon: str):
        """
        Initialize a card with a value, an icon and a color.

        :param value: A string in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"].
        :param icon: A string in ["♥", "♦", "♣", "♠"] that gives the symbol.
        """
        super().__init__(icon)
        self.value = value

    def __str__(self):
        return "value : {}, icon : {}, color : {}".format(self.value, self.icon, self.color)
