// ***********************************************************************************************
// User Story:
// ***********************************************************************************************
// In a substitution cipher, we “encrypt” (i.e., conceal in a reversible way) a message by
// replacing every letter with another letter. To do so, we use a key: in this case, a mapping of
// each of the letters of the alphabet to the letter it should correspond to when we encrypt it.
// To “decrypt” the message, the receiver of the message would need to know the key, so that they
// can reverse the process: translating the encrypt text (generally called ciphertext) back into
// the original message (generally called plaintext).
//
// A key, for example, might be the string NQXPOMAFTRHLZGECYJIUWSKDVB. This 26-character key means
// that A (the first letter of the alphabet) should be converted into N (the first character of
// the key), B (the second letter of the alphabet) should be converted into Q (the second
// character of the key), and so forth.
//
// A message like HELLO, then, would be encrypted as FOLLE, replacing each of the letters
// according to the mapping determined by the key.
//
//


// ***********************************************************************************************
// Requirements:
// ***********************************************************************************************
// In a file called substitution.c in a folder called substitution, create a program that enables
// you to encrypt messages using a substitution cipher. At the time the user executes the program,
// they should decide, by providing a command-line argument, on what the key should be in the
// secret message they’ll provide at runtime.
//
// Design and implement a program, substitution, that encrypts messages using a substitution
// cipher.
//
// 1.- Implement your program in a file called substitution.c in a directory called substitution.
//
// 2.- Your program must accept a single command-line argument, the key to use for the
//     substitution. The key itself should be case-insensitive, so whether any character in the
//     key is uppercase or lowercase should not affect the behavior of your program.
//
// 3.- If your program is executed without any command-line arguments or with more than one
//     command-line argument, your program should print an error message of your choice (with
//     printf) and return from main a value of 1 (which tends to signify an error) immediately.
//
// 4.- If the key is invalid (as by not containing 26 characters, containing any character that
//     is not an alphabetic character, or not containing each letter exactly once), your program
//     should print an error message of your choice (with printf) and return from main a value of
//     1 immediately.
//
// 5.- Your program must output plaintext: (without a newline) and then prompt the user for a
//     string of plaintext (using get_string).
//
// 6.- Your program must output ciphertext: (without a newline) followed by the plaintext’s
//     corresponding ciphertext, with each alphabetical character in the plaintext substituted
//     for the corresponding character in the ciphertext; non-alphabetical characters should be
//     outputted unchanged.
//
// 7.- Your program must preserve case: capitalized letters must remain capitalized letters;
//     lowercase letters must remain lowercase letters.
//
// 8.- After outputting ciphertext, you should print a newline. Your program should then exit by
//     returning 0 from main.
//
//
//

// ***********************************************************************************************
// How to test:
// ***********************************************************************************************
//
//


// ***********************************************************************************************
// My pseudo code approach:
// ***********************************************************************************************
//
//


#include <stdio.h>
#include <ctype.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
// #include <math.h>

// Prototyping Section
bool is_key_valid(string key);
char rotate(string encrypt_key, char letter);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        if (is_key_valid(argv[1]) == false)
        {
            printf("Did not validate\n");
            printf("Usage: %s key\n", argv[0]);
            return 1;
        }
    }
    else
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }

    // If we are here, we have a valid key
    string key = argv[1];
    string phrase = get_string("plaintext: ");
    int phrase_length = strlen(phrase);

    // Now loop through each character
    string ciphertext = phrase;

    char cipher_char;
    for (int i = 0; i < phrase_length; i++)
    {
        // printf("Sending to function character [%c]\n", phrase[i]);
        cipher_char = rotate(key, phrase[i]);
        ciphertext[i] = cipher_char;
    }


    printf("ciphertext: %s\n", ciphertext);
    return 0;
}

bool is_key_valid(string key)
{
    // printf("The key to evaluate is [%s]\n", key);
    // Let's evaluate the length first
    int length = strlen(key);
    if (length != 26)
    {
        printf("Key is NOT 26 characters\n");
        return false;
    }

    // Now lets check that all characters are alphabetical
    for (int i = 0; i < length; i++)
    {
        if (isalpha(key[i]) == false)
        {
            printf("One character is not alpha.  Character is [%c]\n", key[i]);
            return false;
        }
    }

    // Now let's check if a letter is repeated
    int how_many = 0;
    for (int i = 0; i < length; i++)
    {
        how_many = 0;
        for (int j = 0; j < length; j++)
        {
            if (key[i] == key[j])
            {
                how_many += 1;
            }
        }
        if (how_many > 1)
        {
            printf("Character [%c] exists more than once\n", key[i]);
            return false;
        }
    }

    // Now turn them all to uppercase
    for (int i = 0; i < length; i++)
    {
        key[i] = toupper(key[i]);
    }

    printf("Key DID validate\n");
    return true;
}

char rotate(string encrypt_key, char letter)
{
    // Loop through each letter and convert it if it is a letter
    // First let's prime the ciphertext
    char cipher_char =  'A';

    // Assign the phrase to a local string
    string std_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    // printf("The key is [%s]\n", encrypt_key);

    // Get the position of the character against the standard alphabet
    if (islower(letter) || isupper(letter))
    {
        // printf("Will look for index \n");
        for (int i = 0; i < 26; i++)
        {
            // Comparing the letter to each position of the standard array
            if (toupper(letter) == std_alphabet[i])
            {
                // Found that the letters are the same
                // printf("Character [%c] is the same as alphabet [%c]\n", letter, std_alphabet[i]);
                // printf("On index [%i]\n", i);
                if (isupper(letter))
                {
                    // printf("The letter was already upper. cipher_char = [%c]\n", cipher_char);
                    cipher_char = (char) encrypt_key[i];
                    // printf("The letter was already upper. cipher_char = [%c]\n", cipher_char);
                }
                else
                {
                    // printf("The letter needs to force lower. cipher_char = [%c]\n", cipher_char);
                    cipher_char = (char) tolower(encrypt_key[i]);
                    // printf("The letter needs to force lower. cipher_char = [%c]\n", cipher_char);
                }
                i = 27;
            }
        }
        return cipher_char;
    }
    else
    {
        // printf("Nothing to convert since it is not a letter [%c]\n", letter);
        return letter;
    }
}
