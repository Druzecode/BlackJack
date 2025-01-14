using Blackjack2;
using System.Numerics;

internal class Program
{
    private static void Main(string[] args)
    {
        
        Intro();            //displays intro sequence
        char go;            //continues the game if the user chooses to continue after each round
        int bet = 0;     //amount bet each hand
        bool split = false; //becomes true if the player chooses to split
        Deck d1 = new Deck();            //object deck (used as the only deck in the program
        d1.Shuffle();       //shuffles the deck
        //d1.Display(false);

        Player player = new Player();      //object player
        player.Init();
        Player house = new Player("The House");  //object house
        Game game = new Game();
        
        do                          //start of actual game play
        {
            if (d1.Get_Position() > 40) //shuffles the deck so that the cards will never be repeated
                d1.Shuffle();

            bet += game.Bet(player);     //prompts the player for a bet, and stores it as a double
            game.Deal(player, d1, false);           //deals cards to player
            game.Deal(house, d1, true);          //deals cards to house

            split = game.Choice(player, d1, bet);    //controls the route of the game if player chooses to split
            if (split == true)
            {
                game.Split(player, house, d1, bet);  //split sequence
                split = false;                  //resets the flag
            }
            else                                //course of game if the player does not split
            {
                game.H_Play(house, d1);              //makes decisions for the house
                game.Decision(player, house, d1, bet);   //makes the final game decision after player and house are done
                game.Settle(player, house, bet);     //resets the bet to 0 after the money was awarded, and resets the players' hands
            }
            go = game.Go_Play();         //continues play if user chooses to

        } while ((go == 'y' || go == 'Y') && player.money >= game.min_bet);  //exits game when user has no more money, or user chooses to quit

        //cout << "Your final total was: $" << player.money << endl;
        //cout << "Thanks for playing\n\n";

        Console.ReadKey();
    }

    private static void Intro()     //displays intro sequence
    {
        string word = "BLACKJACK";

        Console.WriteLine("\t\t\t\tWelcome To:\n");
        for (int x = 0; x < word.Length; x++)
        {
            Thread.Sleep(150);
            Console.Write("\t" + word[x]);
        }
        Console.WriteLine("\n");
        for (int i = 0; i < 10; i++)
        {
            Thread.Sleep(50);
            Console.Write("- ");
            Thread.Sleep(50);
            Console.Write("= ");
            Thread.Sleep(50);
            Console.Write("- ");
            Thread.Sleep(50);
            Console.Write("= ");
        }
        Console.WriteLine("\n");
    }
}