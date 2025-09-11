class Player:
    def __init__(self, name=None, starting_amount=None):
        if(isinstance(name, str) and len(name) > 0):
            self.__name = name
        else:
            self.__name = input("Enter your name: ") or "Player1"
        
        self.__hand =  [] # Initialize an empty list to hold Card objects
        if(starting_amount != None and isinstance(starting_amount, int) and starting_amount > 0):
            self.__money = starting_amount
        else:
            self.__money = 100  # Invalid format, use default value

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
        total = 0
        for c in self.__hand:
            total += c.get_value(False) # get the total, counting all ACES as 11
        if total > 21:
            for c in self.__hand: #one at a time, switch an ace from an 11 to a 1 until
                if c.rank == 0: #ACE
                    total -= 10
                    if total <= 21:
                        break
        return total

    def get_card(self, card):
        self.__hand.append(card)

    def display_cards(self):
        for card in self.__hand:
            card.draw_card()
    
    def reset_hand(self):
        self.__hand = []
    
    def settle_bet(self, bet):
        self.__money += bet

    def win_amount(self, bet):
        self.__money += bet
    
    def lose_amount(self, bet):
        self.__money -= bet