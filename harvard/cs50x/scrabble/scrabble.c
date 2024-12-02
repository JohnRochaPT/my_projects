// ***********************************************************************************************
// User Story:
// ***********************************************************************************************
// In the game of Scrabble, players create words to score points, and the number of points is the
// sum of the point values of each letter in the word.
//
//  [ A ]  [ B ]  [ C ]  [ D ]  [ E ]  [ F ]  [ G ]  [ H ]  [ I ]  [ J ]  [ K ]  [ L ]  [ M ]
//  [ 1 ]  [ 3 ]  [ 3 ]  [ 2 ]  [ 1 ]  [ 4 ]  [ 2 ]  [ 4 ]  [ 1 ]  [ 8 ]  [ 5 ]  [ 1 ]  [ 3 ]
//
//  [ N ]  [ O ]  [ P ]  [ Q ]  [ R ]  [ S ]  [ T ]  [ U ]  [ V ]  [ W ]  [ X ]  [ Y ]  [ Z ]
//  [ 1 ]  [ 1 ]  [ 3 ]  [ 10]	[ 1 ]  [ 1 ]  [ 1 ]  [ 1 ]  [ 4 ]  [ 4 ]  [ 8 ]  [ 4 ]  [ 10]
//
//
//
//
// For example, if we wanted to score the word “CODE”, we would note that the ‘C’ is worth 3
// points, the ‘O’ is worth 1 point, the ‘D’ is worth 2 points, and the ‘E’ is worth 1 point.
// Summing these, we get that “CODE” is worth 7 points.
//
//

// ***********************************************************************************************
// Requirements:
// ***********************************************************************************************
// In a file called scrabble.c in a folder called scrabble, implement a program in C that
// determines the winner of a short Scrabble-like game. Your program should prompt for input
// twice: once for “Player 1” to input their word and once for “Player 2” to input their word.
// Then, depending on which player scores the most points, your program should either print “Player
// 1 wins!”, “Player 2 wins!”, or “Tie!” (in the event the two players score equal points).
//
//


// ***********************************************************************************************
// How to test:
// ***********************************************************************************************
//
//
//



// ***********************************************************************************************
// My pseudo code approach:
// ***********************************************************************************************
// 1.- Prompt the user for two inputs.  "Player 1: " and "Player 2: "
//
// 2.- Load the array of scores, per position based on the value table provided above.  So for
//     position 0, which is supposed to be letter "A", the value would be 1, while letter "B"
//     would have a value of 3.  Notice that it is not 2 but 3.
//
// 3.- Use library ctype.h use function "toupper()" to convert all the letters since the function
//     itself accepts a character and returns it in upper case, if it was in lower case, and the
//     character itself if the character is already in upper case or it is not a letter.
//
// 4.- Compare the scores and declare the winner with a message "Player 1 wins!" if the winner is
//     player 1 or "Player 2 wins!" if the winner is player 2 and "Tied!" if they are both tied.
//
//



// ***********************************************************************************************
// Revision 1 specs:
// ***********************************************************************************************
//
//
//
//


// ***********************************************************************************************
// Revision 1 pseudo approach:
// ***********************************************************************************************
//
//
//


#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
// #include <stdlib.h>

// Prototyping Section
int get_score(int scores[26], string word);
void who_wins(int player1Score, int player2Score);

int main(void)
{
    // I am going to create an array, in main, because it is passed by reference so I can
    // populate it as well as read it in main or any other function that main calls where the
    // array is passed
    int scores[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1,
                      1, 1, 1, 4, 4, 8, 4, 10};

    string player1Word = get_string("Player 1: ");
    string player2Word = get_string("Player 2: ");

    int player1Score = 0, player2Score = 0;
    player1Score = get_score(scores, player1Word);
    player2Score = get_score(scores, player2Word);

    who_wins(player1Score, player2Score);
}

int get_score(int scores[26], string word)
{
    // The first thing I want to do is to find the length of the string
    int strLength = strlen(word);
    // printf("The length of the string is %i\n", strLength);

    int score = 0;
    for (int i = 0; i < strLength; i++)
    {
        // printf("The iteration loop is [%i]\n", i);
        // printf("The letter is [%c]\n", word[i]);
        // printf("The integer representation of the letter is [%i]\n", word[i]);

        // Convert the character to upper
        word[i] = toupper(word[i]);
        if (isalpha(word[i]))
        {
            score = score + scores[(int) word[i] - 65];
        }
    }
    // printf("The score is [%i]\n", score);
    return score;
}

void who_wins(int player1Score, int player2Score)
{
    if (player1Score == player2Score)
    {
        printf("Tied!\n");
    }
    else if (player1Score > player2Score)
    {
        printf("Player 1 wins!\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }

}
