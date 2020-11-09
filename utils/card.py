
class Symbol:
    def __init__(self, icon: str = ["♥", "♦", "♣", "♠"]):
        self.icon = icon
        if icon == "♥" or icon == "♦":
            self.color = "red"
        else :
            self.color = "black"

class Card(Symbol):
    def __init__(self, value: str, icon: str):
        super().__init__(icon)
        self.value = value

test = Symbol()
print(test.color)
print(test.icon)

test1 = Card("K", "♥")
print(test1.value)
print(test1.color)
print(test1.icon)