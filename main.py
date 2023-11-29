from game import Game

def main():
    # Define the player names
    player_names = ["Alice", "Bob", "Charlie"]

    # Initialize the game with the players
    game = Game(player_names)

    while not game.end_game():
        # Current player's turn
        current_player = game.players[game.turn]
        print(f"\n{current_player.name}'s turn:")

        # Start the turn for the current player
        current_player.start_turn()

        # Simulate player actions
        # This part would include player decisions for playing cards, buying cards, etc.
        # For demonstration purposes, we'll simplify this part
        # Example: current_player.play_card(0), current_player.buy_card(some_card)

        # End the current player's turn
        current_player.end_turn()

        # Proceed to the next turn
        game.next_turn()

    # When the game ends, determine the winner
    winner_message = game.get_winner()
    print("\nGame Over!")
    print(winner_message)

if __name__ == "__main__":
    main()
