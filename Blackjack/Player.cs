using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Blackjack2
{
    internal class Player
    {
        public string name { get; private set; }         //player's name
        public int num_of_cards { get; set; }   //number of cards in the player's hand
        public Card[] hand { get; private set; }       //the actual cards in the player's hand
        public int total { get; set; }          //the total value of the cards in the player's hand
        public double money { get; set; }		//the player's amount of money available to bet


        public Player(int starting_amount = 100)
        {
            hand = new Card[5];

            num_of_cards = 0;   //sets initial amount of cards in hand to 0
            money = starting_amount;        //sets intiial amount of money to 100;
            total = 0;			//total value of cards in hand, initially set to 0
        }

        public Player(string n, int starting_amount = 100) : this(starting_amount)
        {
            name = n;
        }

        public void Init()
        {
            Console.Write("Enter your player's name: ");
            name = Console.ReadLine() ?? "Player1";
        }

        public void GetCard(Deck d1)
        {
            hand[num_of_cards] = d1.SendCard();
            num_of_cards++;
        }

        public void DisplayCards()
        {
            int x = 0;
            while (x < num_of_cards)
            {
                hand[x].Draw_Card();
                x++;
            }
        }

    }
}
