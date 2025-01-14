using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Net.NetworkInformation;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using static System.Reflection.Metadata.BlobBuilder;

namespace Blackjack2
{
    internal class Card
    {
        public enum Suit { Hearts = 1, Diamonds, Clubs, Spades };
        public enum Rank { Ace = 1, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King };
        public Suit suit;
        public Rank rank;


        public Card()
        {
        	rank = Rank.Ace;		//default original rank
	        suit = Suit.Hearts;	    //default original suit
        }

    public void Display_Card()   //displays a card in text
    {
            Console.Write($"{rank} of {suit}");
    }

    public void Set_Suit(int x)      //sets a card's suit
    {
        if (x == 1)
            suit = Suit.Hearts;
        else if (x == 2)
            suit = Suit.Diamonds;
        else if (x == 3)
            suit = Suit.Clubs;
        else if (x == 4)
            suit = Suit.Spades;
        else
            Console.Write("Error");
    }

    public void Set_Rank(int x)      //sets a card's rank
    {
        rank = (Rank)x;
    }

    public int Get_Value(bool flag)     //returns the value of a card
    {
        if (rank == Rank.Ace)
            if (flag == true)           //flag is true if total is over 21, and an Ace must be counted as a 1
            {
                return 1;
                flag = false;           //reset flag, to accommodate multiple aces in one hand
            }
            else
                return 11;              //by default, aces are counted as 11 originally
        else if (rank == Rank.Two)
            return 2;
        else if (rank == Rank.Three)
            return 3;
        else if (rank == Rank.Four)
            return 4;
        else if (rank == Rank.Five)
            return 5;
        else if (rank == Rank.Six)
            return 6;
        else if (rank == Rank.Seven)
            return 7;
        else if (rank == Rank.Eight)
            return 8;
        else if (rank == Rank.Nine)
            return 9;
        else if (rank == Rank.Ten)
            return 10;
        else if (rank == Rank.Jack)
            return 10;
        else if (rank == Rank.Queen)
            return 10;
        else if (rank == Rank.King)
            return 10;
        else
            return 0;
    }

        public string Get_DisplayRank()     //returns the display value of a card
        {
            if (rank == Rank.Ace)
                return "A ";
            else if (rank == Rank.Two)
                return "2 ";
            else if (rank == Rank.Three)
                return "3 ";
            else if (rank == Rank.Four)
                return "4 ";
            else if (rank == Rank.Five)
                return "5 ";
            else if (rank == Rank.Six)
                return "6 ";
            else if (rank == Rank.Seven)
                return "7 ";
            else if (rank == Rank.Eight)
                return "8 ";
            else if (rank == Rank.Nine)
                return "9 ";
            else if (rank == Rank.Ten)
                return "10";
            else if (rank == Rank.Jack)
                return "J ";
            else if (rank == Rank.Queen)
                return "Q ";
            else if (rank == Rank.King)
                return "K ";
            else
                return "  ";
        }
        public char Get_DisplaySuit()
        {
            if (suit == Suit.Hearts)
                return 'H';
            if (suit == Suit.Diamonds)
                return 'D';
            if (suit == Suit.Clubs)
                return 'C';
            if (suit == Suit.Spades)
                return 'S';
            else
                return 'X';
        }

        public void Draw_Back()              //draws the back of a card (for hold cards)
        {
            Console.Write($"\t┌───────────┐\n");
            Console.Write($"\t│***********│\n");
            Console.Write($"\t│***********│\n");
            Console.Write($"\t│***********│\n");
            Console.Write($"\t│***********│\n");
            Console.Write($"\t│***********│\n");
            Console.Write($"\t│***********│\n");
            Console.Write($"\t│***********│\n");
            Console.Write($"\t│***********│\n");
            Console.Write($"\t│***********│\n");
            Console.Write($"\t└───────────┘\n");

            Console.Write("\tHold Card");
            Console.WriteLine("\n");
        }

        public void Draw_Card()          //draws a specific card's picture
        {

            Console.Write($"\t┌───────────┐\n");
            Console.Write($"\t│ {Get_DisplayRank()}        │\n");
            Console.Write($"\t│           │\n");
            Console.Write($"\t│           │\n");
            Console.Write($"\t│           │\n");
            Console.Write($"\t│     {Get_DisplaySuit()}     │\n");
            Console.Write($"\t│           │\n");
            Console.Write($"\t│           │\n");
            Console.Write($"\t│           │\n");
            Console.Write($"\t│        {Get_DisplayRank()} │\n");
            Console.Write($"\t└───────────┘\n");

            Console.Write("\t");
            Display_Card();
            Console.WriteLine("\n");
        }
    }
}
