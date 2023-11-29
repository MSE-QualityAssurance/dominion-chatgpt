class Game:
    def __init__(self, players):
        self.players = [Player(name) for name in players]
        self.supply = self.setup_supply()
        self.turn = 0

    def setup_supply(self):
        # Initialize game supply here

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    def end_game(self):
        # Game ends if all Province cards are gone
        if self.supply["Province"] == 0:
            return True

        # Game also ends if three or more supply piles are empty
        empty_piles = sum(1 for pile in self.supply.values() if pile == 0)
        if empty_piles >= 3:
            return True

        return False

    def get_winner(self):
        max_points = -1
        winners = []
        
        for player in self.players:
            points = player.calculate_victory_points()
            if points > max_points:
                max_points = points
                winners = [player]
            elif points == max_points:
                winners.append(player)

        if len(winners) == 1:
            return f"The winner is {winners[0].name} with {max_points} points!"
        else:
            winner_names = ', '.join([player.name for player in winners])
            return f"It's a tie between {winner_names} with {max_points} points each!"

    # Other methods for gameplay
