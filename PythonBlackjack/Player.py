class Player:
    def __init__(self, name=None, starting_amount=100):
        if(isinstance(name, str) and len(name) > 0):
            self.__name = name
        else:
            self.__name = input("Enter your player's name: ") or "Player1"
        
        self.__hand =  [] # Initialize an empty list to hold Card objects
        self.__money = starting_amount  # Player's money

    @property
    def name(self):
        return self.__name
    
    @property
    def money(self):
        return self.__money

    @property
    def hand(self):
        return self.__hand

    @property
    def num_of_cards(self):
        return len(self.__hand)
    
    @property
    def total(self):
        return len(self.__hand)

    def get_card(self, deck):
        self.__hand.append(deck.get_top_card())

    def display_cards(self):
        for card in self.__hand:
            card.draw_card()
    
    def reset_hand(self):
        self.__hand = []
    
    def win_amount(self, bet):
        self.__money += bet
    
    def lose_amount(self, bet):
        self.__money -= bet