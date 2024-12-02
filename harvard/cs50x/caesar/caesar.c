// ***********************************************************************************************
// User Story:
// ***********************************************************************************************
// Supposedly, Caesar (yes, that Caesar) used to “encrypt” (i.e., conceal in a reversible way)
// confidential messages by shifting each letter therein by some number of places. For instance,
// he might write A as B, B as C, C as D, …, and, wrapping around alphabetically, Z as A. And so,
// to say HELLO to someone, Caesar might write IFMMP instead. Upon receiving such messages from
// Caesar, recipients would have to “decrypt” them by shifting letters in the opposite direction
// by the same number of places.
//
// The secrecy of this “cryptosystem” relied on only Caesar and the recipients knowing a secret,
// the number of places by which Caesar had shifted his letters (e.g., 1). Not particularly
// secure by modern standards, but, hey, if you’re perhaps the first in the world to do it,
// pretty secure!
//
// Unencrypted text is generally called plaintext. Encrypted text is generally called
// ciphertext. And the secret used is called a key.
//
// To be clear, then, here’s how encrypting HELLO with a key of 1 yields IFMMP:
//
//          plaintext       [ H ]  [ E ]  [ L ]  [ L ]  [ O ]
//          + key           [ 1 ]  [ 1 ]  [ 1 ]  [ 1 ]  [ 1 ]
//          = ciphertext	[ I ]  [ F ]  [	M ]  [ M ]	[ P ]
//


// ***********************************************************************************************
// Requirements:
// ***********************************************************************************************
// In a file called caesar.c in a folder called caesar, write a program that enables you to
// encrypt messages using Caesar’s cipher. At the time the user executes the program, they should
// decide, by providing a command-line argument, what the key should be in the secret message
// they’ll provide at runtime. We shouldn’t necessarily assume that the user’s key is going to be
// a number; though you may assume that, if it is a number, it will be a positive integer.
//
// 1.- Implement your program in a file called caesar.c in a directory called caesar.
//
// 2.- Your program must accept a single command-line argument, a non-negative integer. Let’s call
//     it for the sake of discussion.
//
// 3.- If your program is executed without any command-line arguments or with more than one
//     command-line argument, your program should print an error message of your choice (with
//     printf) and return from main a value of 1 (which tends to signify an error) immediately.
//
// 4.- If any of the characters of the command-line argument is not a decimal digit, your program
//     should print the message Usage: ./caesar key and return from main a value of 1.
//
// 5.- Do not assume that "k" will be less than or equal to 26. Your program should work for all
//     non-negative integral values of "k" less than 2(P31) - 26.  In other words, you don’t need
//     to worry if your program eventually breaks if the user chooses a value for "k" that’s too
//     big or almost too big to fit in an int. (Recall that an int can overflow.) But, even if
//     "k" is greater than 26, alphabetical characters in your program’s input should remain
//     alphabetical characters in your program’s output. For instance, if "k" is 27, A should
//     not become \ even though \ is 27 positions away from A in ASCII, per asciitable.com; A
//     should become B, since B is 27 positions away from A, provided you wrap around from Z
//     to A.
//
// 6.- Your program must output plaintext: (with two spaces but without a newline) and then prompt
//     the user for a string of plaintext (using get_string).
//
// 7.- Your program must output ciphertext: (with one space but without a newline) followed by the
//     plaintext’s corresponding ciphertext, with each alphabetical character in the plaintext
//     “rotated” by k positions; non-alphabetical characters should be outputted unchanged.
//
// 8.- Your program must preserve case: capitalized letters, though rotated, must remain
//     capitalized letters; lowercase letters, though rotated, must remain lowercase letters.
//
// 9.- After outputting ciphertext, you should print a newline. Your program should then exit by
//     returning 0 from main.
//

// ***********************************************************************************************
// Requirements: Counting Command-Line Arguments
// ***********************************************************************************************
// Whatever your pseudocode, let’s first write only the C code that checks whether the program was
// run with a single command-line argument before adding additional functionality.
//
// Specifically, modify main in caesar.c in such a way that, if the user provides no command-line
// arguments, or two or more, the function prints "Usage: ./caesar key\n" and then returns 1,
// effectively exiting the program. If the user provides exactly one command-line argument, the
// program should print nothing and simply return 0. The program should thus behave per the below.
//
//          $ ./caesar
//          Usage: ./caesar key
//
//          $ ./caesar 1 2 3
//          Usage: ./caesar key
//
//          $ ./caesar 1
//
//


// ***********************************************************************************************
// Requirements: Checking the Key
// ***********************************************************************************************
// Now that your program is (hopefully!) accepting input as prescribed, it’s time for another
// step.
//
// Add to caesar.c, below main, a function called, e.g., only_digits that takes a string as an
// argument and returns true if that string contains only digits, 0 through 9, else it returns
// false. Be sure to add the function’s prototype above main as well.
//
//


// ***********************************************************************************************
// Requirements: Using the Key
// ***********************************************************************************************
// Now modify main in such a way that it converts argv[1] to an int. You might find atoi, declared
// in stdlib.h, to be helpful, per manual.cs50.io. And then use get_string to prompt the user for
// some plaintext with "plaintext: ".
//
// Then, implement a function called, e.g., rotate, that takes a char as input and also an int,
// and rotates that char by that many positions if it’s a letter (i.e., alphabetical), wrapping
// around from Z to A (and from z to a) as needed. If the char is not a letter, the function
// should instead return the same char unchanged.
//
//


// ***********************************************************************************************
// Additional Requirements
// ***********************************************************************************************
// 1.- Get key
//
// 2.- Get plaintext
//
// 3.- Encipher
//
// 4.- Print ciphertext
//
// 5.- Preserve case
//
// 6.- Only shift alpha characters.  Do not shift spaces or numbers or non alpha characters
//
// 7.- Must accept a command line argument where there is only one argument and that the argument
//     is an integer.  Must not contain a floating point.  Use atoi function
//
// 8.- Formula is C = (P + K) % 26
//



// ***********************************************************************************************
// My pseudo code approach:
// ***********************************************************************************************

//
//
//
//
//
//
//
//
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


#include <stdio.h>
#include <ctype.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
// #include <math.h>

// Prototyping Section
bool only_digits(char letter);
char rotate(char letter, int key);

int main(int argc, string argv[])
{
    // printf("How many [%i]\n", argc);
    // printf("The second one [%s]\n", argv[1]);
    // Validate the key value
    int key = 0;
    if (argc == 2)
    {
        string argument = argv[1];
        int length = strlen(argument);
        for (int i = 0; i < length; i++)
        {
            // printf("Argument letter [%i] is [%c]\n",i, argument[i]);
            if (only_digits(argument[i]) == false)
            {
                printf("%s key\n", argv[0]);
                return 1;
            }
        }
       key = atoi(argv[1]);
    }
    else
    {
        printf("%s key\n", argv[0]);
        return 1;
    }

    // printf("The key is [%i]\n", key);
    // Get the text
    string clear_text = get_string("Text: ");
    printf("ciphertext: ");

    int length = strlen(clear_text);
    char c;
    for (int i = 0; i < length; i++)
    {
        c = rotate(clear_text[i], key);
        printf("%c", c);
    }

    printf("\n");
    return 0;

}

bool only_digits(char letter)
{
    // Can't use atoi() because atoi() expects a string.  Not a character.
    if (isdigit(letter))
    {
        //printf("It IS numeric\n");
        return true;
    }
    else
    {
        //printf("It is NOT numeric\n");
        return false;
    }
}

char rotate(char letter, int key)
{
    // Rotate only if a letter
    int lower = 97, upper = 65;
    char encrypted;
    if (isupper(letter))
    {
        encrypted = (((letter - upper) + key) % 26) + upper;
    }
    else if (islower(letter))
    {
        encrypted = (((letter - lower) + key) % 26) + lower;
    }
    else
    {
        encrypted = letter;
    }

    return encrypted;

}


