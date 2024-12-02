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

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // printf("Passing through function [%s]\n", input);
    char c;
    int last_int, length = 2;
    bool one_more = true;

    // Find the base.  The base is where the iteration of i returns no character at pos 2
    c = (char) input[1];
    if (!c)
    {
        return (int) input[0] - 48;
    }

    while (one_more)
    {
        c = (char) input[length];
        if (c)
        {
            length += 1;
        }
        else
        {
            one_more = false;
        }
    }

    // printf("The last position is [%i]\n", length);
    last_int = (int) input[length - 1] - 48;
    input[length - 1] = '\0';

    return last_int + 10 * convert(input);
}
