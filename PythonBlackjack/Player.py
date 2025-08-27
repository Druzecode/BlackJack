class Player:
    def __init__(self, name="", starting_amount=100):
        if(name == ""):
            self.name = input("Enter your player's name: ") or "Player1"
        else:
            self.name = name
        
        self.num_of_cards = 0  # Number of cards in the player's hand
        self.hand =  [] # Initialize an empty list to hold Card objects
        self.total = 0  # Total value of cards in hand
        self.money = starting_amount  # Player's money

    def get_card(self, deck):
        self.hand.append(deck.send_card())
        self.num_of_cards += 1

    def display_cards(self):
        for card in self.hand:
            card.draw_card()