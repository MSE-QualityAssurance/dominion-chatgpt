class Game:
    def __init__(self, players):
        self.players = [Player(name) for name in players]
        self.supply = self.setup_supply()
        self.turn = 0

    def setup_supply(self):
        # Initialize game supply here

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    # Other methods for gameplay
