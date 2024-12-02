//.*************************************************************************************************
//. User Story:
//.*************************************************************************************************
/// Imagine that you travel back in time to the 1970’s, when the C programming language was first
/// created. You are hired as a programmer to come up with a way to convert strings to ints. (You
/// may have used a function just like this in Week 2, called atoi). You want to be thorough in
/// your development process and plan to try several approaches before deciding on the most
/// efficient.
///
/// In this problem, you will start with a simple implementation of atoi that handles positive ints
/// using loops. You want to rework this into an implementation that uses recursion. Recursive
/// functions can be memory intensive and are not always the best solution, but there are some
/// problems in which using recursion can provide a simpler and more elegant solution.
///
/// (Scroll to the bottom of this page to see what an implementation of atoi might actually look
/// like.)
///


//.*************************************************************************************************
//. Requirements:
//.*************************************************************************************************
/// 1.- Start by getting the index of the last char in the string (the char before the \0).
///
/// 2.- Convert this char into its numeric value. Can you subtract some char to do this?
///
/// 3.- Remove the last char from the string by moving the null terminator one position to the left.
///
/// 4.- Return this value plus 10 times the integer value of the new shortened string.
///
/// 5.- Remember you need a base case when creating a recursive function.
///


#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    string word = get_string("Input a string: ");


    // Convert string to int
    int length = 0;
    int character = 0;
    int result = 0;

    if ((length = strlen(word)) > 3)
    {
        length = 3;
    }

    for (int i = 0; i < length; i++)
    {
        printf("Character [%c] as integer[%i]\n", toupper(word[i]), toupper(word[i]));
        if ((toupper(word[i]) - 65) < 0 )
        {
            character = 0;
        }
        else
        {
            character = toupper(word[i]) - 65;
        }
        result = result * length + character;
        /// printf("The converted character is [%i]\n", character);
        /// printf("The running total is [%i]\n", result);
    }

    printf("The hashed number is [%i]\n", result);
}
