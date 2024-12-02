//.*************************************************************************************************
//. User Story:
//.*************************************************************************************************
/// Your function will iterate through the password that’s supplied to it as an argument. Since you
/// have to find at least one lower case letter, one upper case letter, one number and one symbol,
/// you may want to create a boolean variable for each and set each to false before you iterate
/// through the string. If you then find a number, for instance you can set that boolean to true. If
/// all booleans are true at the end of the function, it means all criteria are met, and you would
/// return true.
///

//.*************************************************************************************************
//. How to test:
//.*************************************************************************************************
/// 1.- Sample:
//>     password/ $ ./password
//>     Enter your password: hello
//>     Your password needs at least one uppercase letter, lowercase letter, number and symbol!
///
/// 2.- Sample:
//>     password/ $ ./password
//>     Enter your password: h3ll(
//>     Your password needs at least one uppercase letter, lowercase letter, number and symbol!
///
/// 3.- Sample:
//>     password/ $ ./password
//>     Enter your password: h3LL0!
//>     Your password is valid!
///

// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    // An uppercase letter
    bool has_upper = false, has_lower = false, has_number = false, has_symbol = false;
    int length = strlen(password);
    for (int i = 0; i < length; i++)
    {
        //< If the conditions have been met, end the loop
        if (has_upper && has_lower && has_symbol && has_number)
        {
            return true;
        }

        //< Check to see if it is alpha if no, then check to see if it is a digit
        //< Then, check to see if it is a symbol.  While the range includes letters
        //< and numbers, we would not get to the last if, if it is a printable character
        //< and it is not alpha, it is not numeric either so now, if it falls in the range
        //< then it is a printable character.

        //< No need to check upper or lower if they are already true
        //- printf("Start of checking character [%c]\n", password[i]);
        //- printf("--- Is [%c] alpha?\n", password[i]);
        if (!has_upper || !has_lower)
        {
            if (isalpha(password[i]))
            {
                if (isupper(password[i]))
                {
                    has_upper = true;
                }
                else
                {
                    has_lower = true;
                }
            }
        }
        else if (isdigit(password[i]))
        {
            has_number = true;
        }
        else
        {
            if ((((int) password[i] > 32) && ((int) password[i] <= 47)) ||
                (((int) password[i] >= 58) && ((int) password[i] <= 64)) ||
                (((int) password[i] >= 91) && ((int) password[i] <= 96)) ||
                (((int) password[i] >= 123) && ((int) password[i] <= 126)) )
            {
                has_symbol = true;
            }
        }
    }
    return (has_upper && has_lower && has_symbol && has_number);
}
