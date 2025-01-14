using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Blackjack2
{
    internal class Deck
    {
        Card[] cards = new Card[52];     //array of 52 cards - a full deck
        int position;

        public Deck()
        {
	        position = 0;	//beginning of deck
	        int y = 0;
            for (int count = 1; count <= 4; count++)    //gives a value to each card in the deck (ordered by suit than rank)
            {
                for (int i = 1; i <= 13; i++)
                {
                    cards[y] = new Card();
                    cards[y].Set_Rank(i);
                    cards[y].Set_Suit(count);
                    y++;
                }
            }
        }
        public void Shuffle()	//shuffles the deck
        {
            Random rnd = new Random();
            int x, y;           //random numbers
            Card temp;          //temporary card holder
            for (int i = 0; i < 300; i++)
            {
                x = rnd.Next(0, 51); //places a random card in the temp holder
                temp = cards[x];
                y = rnd.Next(0, 51); //moves a random card to the original card's place
                cards[x] = cards[y];
                cards[y] = temp;        //places the temp card into the moved cards place
            }
            position = 0;		//resets the pointer to the start of the deck
        }

        public void Display(bool draw_cards = false)	//displays all of the cards in the deck (not used in the actual game)
        {
            for (int i = 0; i < 52; i++)
            {
                if(draw_cards)
                    cards[i].Draw_Card();    //displays text value for each card (e.g. "nine of hearts")
                else
                    cards[i].Display_Card();
                Console.WriteLine();
            }
            Console.WriteLine("\n\n");
        }

        public Card SendCard()		//returns the "top" card on the deck
        {
            position++;         //points to next card
            return cards[position - 1]; //returns previous card

        }

        public int Get_Position()	//returns the position in the deck
        {
            return position;
        }
    }
}
