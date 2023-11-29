class Card:
    def __init__(self, name, card_type, cost):
        self.name = name
        self.card_type = card_type
        self.cost = cost


class TreasureCard(Card):
    def __init__(self, name, cost, value):
        super().__init__(name, "Treasure", cost)
        self.value = value


class VictoryCard(Card):
    def __init__(self, name, cost, points):
        super().__init__(name, "Victory", cost)
        self.points = points

class ActionCard(Card):
    def __init__(self, name, cost):
        super().__init__(name, "Action", cost)
    # Action cards will need methods to define their special actions

