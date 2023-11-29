class Game:
    def __init__(self, players):
        self.players = [Player(name) for name in players]
        self.supply = self.setup_supply()
        self.turn = 0

    def setup_supply(self):
        # Basic setup for 2-4 players
        num_players = len(self.players)

        # Set up standard Victory and Treasure cards
        supply = {
            "Copper": 60 - (7 * num_players),  # Each player starts with 7 Coppers
            "Silver": 40,
            "Gold": 30,
            "Estate": 12 if num_players == 2 else 24,  # 8 per player for 2 players, otherwise 12
            "Duchy": 12,
            "Province": 12,
            "Curse": (num_players - 1) * 10  # 10 per additional player
        }

        # Add a predefined set of 10 Kingdom cards
        kingdom_cards = ["Smithy", "Village", "Market", "Militia", "Mine",
                         "Moat", "Remodel", "Cellar", "Workshop", "Laboratory"]
        for card in kingdom_cards:
            supply[card] = 10  # Standard number of each Kingdom card

        return supply

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
