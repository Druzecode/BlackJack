using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace Blackjack2
{
    internal class Game
    {
        public int min_bet = 5;

        public int Bet(Player player)
        {
            int bet = 0;
            do
            {
                Console.WriteLine($"You currently have ${player.money}");
                Console.Write("How much would you like to bet? $");

                if (!int.TryParse(Console.ReadLine(), out bet))
                    Console.WriteLine("Invalid amount entered\n");
                else if (bet > player.money)
                    Console.WriteLine("You do not have that much money!\n");
                else if (bet <= 5)
                    Console.WriteLine($"You must enter a valid bet (minimum ${min_bet})!\n");
                else
                    Console.WriteLine();
            } while (bet > player.money || bet < min_bet);      //reprompts user if an invalid input is entered

            Console.Clear();
            return bet;
        }

        public void Deal(Player player, Deck d1, bool hide_card)     //deals cards to the player's hand
        {
            Console.WriteLine($"{player.name} has: ");
            player.hand[player.num_of_cards] = d1.SendCard();   //gets first card
            player.hand[player.num_of_cards].Draw_Card();       //displays first card
            player.num_of_cards++;                  //increments the number of cards in the player's hand

            player.hand[player.num_of_cards] = d1.SendCard();   //gets the second card
            if(hide_card)
                player.hand[player.num_of_cards].Draw_Back();
            else
                player.hand[player.num_of_cards].Draw_Card();       //displays the second card
            
            player.num_of_cards++;                  //increments the number of cards in the player's hand

            Thread.Sleep(3000);
            Console.Clear();                      //clears screen
        }

        public bool Choice(Player player, Deck d1, int bet)
        {
            bool cont = true;       //continues
            bool split = false;     //becomes true when the split function is chosen
            while (cont == true)
            {
                player.total = 0;   //resets player's total to 0 before it is recalculated
                int choice = 0;     //player's choice (entered later)
                bool flag = false;  //true if cards in hand total over 21
                cont = false;       //resets the continue flag
                int x = 0;          //counting variable
                Console.Clear();      //clears screen
                Console.WriteLine($"{player.name}, you have the: ");
                while (x < player.num_of_cards)     //displays player's cards and calculates the player's total
                {
                    Console.Write("\t");
                    player.hand[x].Display_Card();
                    Console.WriteLine();
                    player.total += player.hand[x].Get_Value(flag);
                    x++;
                }
                if (player.total > 21)  //recalculates total if ace must be set to 1 instead of 11
                {
                    x = 0;                  //resets counting variable
                    player.total = 0;       //resets total for new count 
                    while (x < player.num_of_cards)
                    {
                        flag = true;
                        player.total += player.hand[x].Get_Value(flag);
                        x++;
                    }
                }
                if (player.total > 21)  //recalculates total if ace must be set to 1 instead of 11
                {
                    x = 0;                  //resets counting variable
                    player.total = 0;       //resets total for new count 
                    while (x < player.num_of_cards)
                    {
                        flag = true;
                        player.total += player.hand[x].Get_Value(flag);
                        x++;
                    }
                }

                Console.WriteLine();
                Console.WriteLine($"You have a total of: {player.total}");
                Console.WriteLine("\n");

                if (player.total <= 21 && player.num_of_cards < 5)  //exits when player is over 21, or over 5 cards
                {
                    if (player.hand[0].rank == player.hand[1].rank && player.num_of_cards == 2 && player.money >= (bet * 2))  //allows split and double down options
                    {
                        if (player.total == 10 || player.total == 11)
                        {
                            do
                            {
                                Console.WriteLine($"Would you like to (1)Hit, (2)Stand, (3)Split, or (4)Double Down? ");    //displays options
                                choice = GetInput();
                                Console.WriteLine();
                                if (choice < 1 || choice > 4)
                                    Console.WriteLine($"Please make another selection\n");
                            } while (choice < 1 || choice > 4);     //continues on invalid selections
                        }
                        else    //allows split option
                        {
                            do
                            {
                                Console.WriteLine($"Would you like to (1)Hit, (2)Stand, or (3)Split? ");            //displays options
                                choice = GetInput();
                                Console.WriteLine();
                                if (choice < 1 || choice > 3)
                                    Console.WriteLine($"Please make another selection\n");
                            } while (choice < 1 || choice > 3);     //continues on invalid inputs
                        }
                    }
                    else if (player.hand[0].rank != player.hand[1].rank && (player.total == 10 || player.total == 11) && player.num_of_cards == 2)  //allows double down option
                    {
                        do
                        {
                            Console.WriteLine($"Would you like to (1)Hit, (2)Stand, or (3)Double Down? ");      //displays options
                            choice = GetInput();
                            Console.WriteLine();
                            if (choice < 1 || choice > 3)
                                Console.WriteLine($"Please make another selection\n");
                        } while (choice < 1 || choice > 3); //continues on invalid selection
                        if (choice == 3)
                            choice = 4;     //sets proper value to double down selection, to prevent from calling split function
                    }
                    else
                    {
                        do
                        {
                            Console.WriteLine($"Would you like to (1)Hit or (2)Stand? ");       //normal options
                            choice = GetInput();
                            Console.WriteLine();
                            if (choice < 1 || choice > 2)
                                Console.WriteLine($"Please make another selection\n");
                        } while (choice < 1 || choice > 2); //continues on invalid input
                    }
                }
                else
                    choice = 2;

                if (choice == 1)
                {
                    Hit(player, d1);        //calls hit function if selected
                    cont = true;
                }
                else if (choice == 3)
                {
                    split = true;           //calls split function if chosen
                    cont = false;
                }
                else if (choice == 4)
                {
                    DoubleDown(player, d1, bet);    //calls double down function if chosen
                    cont = false;
                }
            }
            return split;       //returns true if split is selected
        }

        private int GetInput()
        {
            int validInput = 0;
            var input = Console.ReadLine();
            if (int.TryParse(input, out validInput))
                return validInput;
            else
                return 0;
        }

        public void Hit(Player player, Deck d1)
        {
            Console.Clear();      //clears screen

            Console.WriteLine($"{player.name} received the ");
            player.hand[player.num_of_cards] = d1.SendCard();   //gets a new card from the deck
            player.hand[player.num_of_cards].Draw_Card();       //displays new card
            player.num_of_cards++;          //increments number of cards in hand

            Thread.Sleep(2000);   //waits 2 seconds
            Console.Clear();
        }

        public void Split(Player player, Player house, Deck d1, int bet)
        {
            Player player2 = new Player(player.name + "'s second hand", 0);       //new object, player's second hand
            player.num_of_cards = 1;
            player2.num_of_cards = 1;
            player2.hand[0] = player.hand[1];   //splits hand
            Hit(player, d1);                    //adds a new card to first hand
            Hit(player2, d1);                   //adds a new card to second hand

            Choice(player, d1, bet);            //plays first hand
            Choice(player2, d1, bet);           //plays second hand

            H_Play(house, d1);                  //house plays

            Console.WriteLine($"First Hand:");
            Decision(player, house, d1, bet);   //decides if first hand wins
            Console.WriteLine($"Second Hand:");
            Decision(player2, house, d1, bet);  //decides if second hand wins
            player.money += (player2.money);

            Settle(player, house, bet);     //resets values from next hand
        }

        public void DoubleDown(Player player, Deck d1, int bet)
        {
            bool x = false;
            Hit(player, d1);    //gives the player one more card
            bet *= 2;           //doubles the bet
            if (player.total == 11)
                x = true;
            player.total += player.hand[2].Get_Value(x);
        }

        public void H_Play(Player house, Deck d1)        //house plays its hand
        {
            bool cont = true;       //continues until house is finished
            while (cont == true)
            {
                house.total = 0;
                bool flag = false;
                cont = false;
                int x = 0;          //counter variable
                Console.Clear();      //clear screen
                Console.WriteLine($"{house.name} has the: ");
                while (x < house.num_of_cards)      //displays house's cards and calculates the total value
                {
                    Console.WriteLine("\t");
                    house.hand[x].Display_Card();       //displays the cards that are in the house's hand
                    Console.WriteLine();
                    house.total += house.hand[x].Get_Value(flag);       //calculates the total value
                    x++;            //increment counter
                }
                if (house.total > 21)       //recounts with ace equal to 1
                {
                    x = 0;
                    house.total = 0;
                    while (x < house.num_of_cards)
                    {
                        flag = true;
                        house.total += house.hand[x].Get_Value(flag);
                        x++;
                    }
                }

                Console.WriteLine();
                Console.Write($"{house.name} has a total of: {house.total}, and chooses to ");
                if (house.total < 17)
                {
                    Console.Write("hit\n");
                    Thread.Sleep(2500);   //wait 2.5 seconds
                    Hit(house, d1);                 //deals another card to the house
                    cont = true;
                }
                else
                    Console.Write("stand\n");
            }
        }

        public void Decision(Player player, Player house, Deck d1, int bet)
        {
            Console.WriteLine($"You have a total of {player.total}\n");

            Thread.Sleep(2000);       //wait 2 seconds

            if (player.total < 21 && player.num_of_cards == 5 && house.num_of_cards != 5)   //if you win five card rule
            {
                Console.WriteLine("You Win! (five card rule)\n");
                player.money += bet;
            }
            else if (house.total < 21 && player.num_of_cards == 5 && player.num_of_cards != 5)  //if you lose five card rule
            {
                Console.WriteLine("You Lose (five card rule)\n");
                player.money -= bet;
            }
            else
            {
                if (player.total == 21 && player.num_of_cards == 2) //if you have a blackjack
                {
                    if (house.total != 21 || house.num_of_cards > 2)    //if you win
                    {
                        Console.WriteLine("You have a BlckJack!\nYou Win!\n");
                        player.money += (bet * 1.5);
                    }
                    else                                                //if house has one too
                    {
                        Console.WriteLine($"Draw\n");
                    }
                }
                else if (house.total == 21 && house.num_of_cards == 2)  //if house has a blackjack
                {
                    Console.WriteLine("The House has a BlckJack!\nYou Lose\n");
                    player.money -= bet;
                }
                else
                {
                    if (player.total > 21)                      //test player for bust
                        Console.WriteLine("You are over!");
                    if (house.total > 21)                       //test house for bust
                        Console.WriteLine("House is over!");
                    if (player.total > 21 && house.total > 21)  //test both for bust
                    {
                        Console.WriteLine("Draw\n");
                    }
                    else if (player.total > 21 && house.total <= 21)    //if player is over
                    {
                        Console.WriteLine("You Lose\n");
                        player.money -= bet;
                    }
                    else if (house.total > 21 && player.total <= 21)    //if house is over
                    {
                        Console.WriteLine("You Win!\n");
                        player.money += bet;
                    }
                    else if (house.total <= 21 && player.total <= 21)   //both are under
                    {
                        if (house.total < player.total)                 //if player beats house in points
                        {
                            Console.WriteLine("You Win!\n");
                            player.money += bet;
                        }
                        else if (house.total > player.total)            //if house beats player in points
                        {
                            Console.WriteLine("You Lose\n");
                            player.money -= bet;
                        }
                        else                                            //if tie with points
                        {
                            if (player.num_of_cards < house.num_of_cards)   //if player has fewer cards than house
                            {
                                Console.WriteLine($"You Win! (Fewer Cards)\n");
                                player.money += bet;
                            }
                            else if (player.num_of_cards > house.num_of_cards)  //if player has more cards than house
                            {
                                Console.WriteLine($"You Lose (House has fewer cards)\n");
                                player.money -= bet;
                            }
                            else                                                //both are equal (draw)
                                Console.WriteLine($"Draw\n");
                        }
                    }
                }
            }
        }

        public void Settle(Player player, Player house, int bet)
        {
            player.num_of_cards = 0;        //resets player's hand
            house.num_of_cards = 0;         //resets house's hand
            bet = 0;                        //resets bet
        }

        public char Go_Play()
        {
            char go;        //variable to continue
            Console.WriteLine("Would you like to continue(y/n)? ");
            go = Console.ReadKey().KeyChar;
            Console.Clear();      //clear screen
            return go;          //returns user's input
        }
    }
}
