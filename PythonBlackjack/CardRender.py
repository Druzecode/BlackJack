import os

class CardRender:
    def __init__(self):
        try:
            size = os.get_terminal_size()
            columns = size.columns
            rows = size.lines
        except OSError:
            columns = 80  # default width
            rows = 24     # default height

        print(f"Columns: {columns}, Rows: {rows}")

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
        print(f"\t│ {card.get_display_rank()}        │")
        print("\t│           │")
        print("\t│           │")
        print("\t│           │")
        print(f"\t│     {card.get_display_suit()}     │")
        print("\t│           │")
        print("\t│           │")
        print("\t│           │")
        print(f"\t│        {card.get_display_rank()} │")
        print("\t└───────────┘")

        print("\t", end="")
        card.display_card_as_text()
        print("\n")