

class CardRender:
    def __init__(self):
        pass

    def draw_back(self, card):  # draws the back of a card (for hold cards)
        print("\t┌───────────┐")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t└───────────┘")

        print("\tHold Card")
        print("\n")

    def draw_card(self, card):  # draws a specific card's picture
        print("\t┌───────────┐")
        print(f"\t│ {card.get_display_rank()}         │")
        print("\t│           │")
        print("\t│           │")
        print("\t│           │")
        print(f"\t│     {card.get_display_suit()}     │")
        print("\t│           │")
        print("\t│           │")
        print("\t│           │")
        print(f"\t│        {card.get_display_rank()}  │")
        print("\t└───────────┘")

        print("\t", end="")
        card.display_card_as_text()
        print("\n")