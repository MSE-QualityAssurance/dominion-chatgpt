import random

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = self.initialize_deck()
        self.hand = []
        self.discard_pile = []
        self.actions = 1
        self.buys = 1
        self.coins = 0

    def initialize_deck(self):
        # Initialize with 7 Coppers and 3 Estates
        return [TreasureCard("Copper", 0, 1)] * 7 + [VictoryCard("Estate", 2, 1)] * 3

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        if not self.deck:
            self.deck, self.discard_pile = self.discard_pile, self.deck
            self.shuffle_deck()
        if self.deck:
            card = self.deck.pop()
            self.hand.append(card)

    def start_turn(self):
        self.actions = 1
        self.buys = 1
        self.coins = 0
        for _ in range(5):
            self.draw_card()

    def play_card(self, card_index):
        if card_index < len(self.hand) and self.hand[card_index].card_type == "Action" and self.actions > 0:
            card = self.hand.pop(card_index)
            # Perform the action associated with the card
            # This will require custom logic based on the card
            self.actions -= 1

    def play_treasure(self, card_index):
        if card_index < len(self.hand) and self.hand[card_index].card_type == "Treasure":
            card = self.hand.pop(card_index)
            self.coins += card.value

    def buy_card(self, card):
        if self.buys > 0 and self.coins >= card.cost:
            self.discard_pile.append(card)
            self.coins -= card.cost
            self.buys -= 1

    def end_turn(self):
        self.discard_pile.extend(self.hand)
        self.hand = []
        for _ in range(5):
            self.draw_card()

    def show_hand(self):
        return [card.name for card in self.hand]


    # Methods for drawing cards, playing cards, etc.
