//.*************************************************************************************************
//. User Story:
//.*************************************************************************************************
/// If you’ve been on the internet, you might have seen “leetspeak” (or “l33tsp36k” for our
/// purposes!), which involves the substitution of symbols for alphabetical characters, where those
/// symbols somewhat resemble their alphabetical counterparts. In this lab, you’ll write a program
/// to replace certain vowels with digits!
///
/// Up until now, you’ve frequently written programs for which you’ve been provided distribution
/// code. You’ll notice when downloading the “distro” for this problem, you start with nothing more
/// than a couple of commonly used libraries and an empty main function. In this problem, you will
/// convert a word, which you will input at the command line, to a corresponding word with numbers
/// replacing vowels.
///
///



//.*************************************************************************************************
//. Requirements:
//.*************************************************************************************************
/// 1.- Implement your program in a file called no-vowels.c in a directory called no-vowels.
///
/// 2.- Your program must accept a single command-line argument, which will be the word that you
///     want to convert.
///
/// 3.- If your program is executed without any command-line arguments or with more than one
///     command-line argument, your program should print an error message of your choice (with
///     printf) and return from main a value of 1 (which tends to signify an error) immediately.
///
/// 4.- Your program must contain a function called replace which takes a string input and returns
///     a string output.
///
/// 5.- This function will change the following vowels to numbers: a becomes 6, e becomes 3, i
///     becomes 1, o becomes 0 and u does not change.
///
/// 6.- The input parameter for the replace function will be argv[1] and the return value is the
///     converted word.
///
/// 7.- The main function will then print the converted word, followed by \n.
///
/// 8.- You may want to try using the switch statement in your replace function.
///
///


//.*************************************************************************************************
//. How to test:
//.*************************************************************************************************
/// 1.- Sample:
//>             no-vowels/ $ ./no-vowels
//>             Usage: ./no-vowels word
///
/// 2.- Sample:
//>             no-vowels/ $ ./no-vowels hello
//>             h3ll0
///
/// 3.- Sample:
//>             no-vowels/ $ ./no-vowels pseudocode
//>             ps3ud0c0d3
///



// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string replace(string word);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s word\n",argv[0]);
        return 1;
    }
    string massage = replace(argv[1]);
    printf("%s\n", massage);
}

string replace(string word)
{
    int length = strlen(word);
    for (int i = 0; i < length; i++)
    {
        switch(toupper(word[i]))
        {
            case 'A':
                word[i] = '6';
                break;
            case 'E':
                word[i] = '3';
                break;
            case 'I':
                word[i] = '1';
                break;
            case 'O':
                word[i] = '0';
                break;
            default:
                break;
        }
    }
    return word;
}
