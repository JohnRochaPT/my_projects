// ****************************************************************************************************
// User Story:
// ****************************************************************************************************
// A credit (or debit) card, of course, is a plastic card with which you can pay for goods and
// services. Printed on that card is a number that’s also stored in a database somewhere, so that
// when your card is used to buy something, the creditor knows whom to bill. There are a lot of
// people with credit cards in this world, so those numbers are pretty long: American Express uses
// 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. And
// those are decimal numbers (0 through 9), not binary, which means, for instance, that American
// Express could print as many as 10^15 = 1,000,000,000,000,000 unique cards! (That’s, um, a
// quadrillion.)
//
// Actually, that’s a bit of an exaggeration, because credit card numbers actually have some
// structure to them. All American Express numbers start with 34 or 37; most MasterCard numbers
// start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we
// won’t concern ourselves with for this problem); and all Visa numbers start with 4. But credit
// card numbers also have a “checksum” built into them, a mathematical relationship between at least
// one number and others. That checksum enables computers (or humans who like math) to detect typos
// (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can
// be slow. Of course, a dishonest mathematician could certainly craft a fake number that
// nonetheless respects the mathematical constraint, so a database lookup is still necessary for
// more rigorous checks.
//
// Luhn’s Algorithm
// So what’s the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of
// IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically)
// valid as follows:
//
//  1.- Multiply every other digit by 2, starting with the number’s second-to-last digit, and then
//  add
//      those products’ digits together.
//  2.- Add the sum to the sum of the digits that weren’t multiplied by 2.
//  3.- If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent
//      to 0), the number is valid!
//
// That’s kind of confusing, so let’s try an example with David’s Visa: 4003600000000014.
//
//  1.- For the sake of discussion, let’s first underline every other digit, starting with the
//  number’s
//      second-to-last digit:
//          4003600000000014
//      Okay, let’s multiply each of the underlined digits by 2:
//          1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2
//      That gives us:
//          2 + 0 + 0 + 0 + 0 + 12 + 0 + 8
//      Now let’s add those products’ digits (i.e., not the products themselves) together:
//          2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
//
//  2.- Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting
//      from the end):
//          13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20
//
//  3.- Yup, the last digit in that sum (20) is a 0, so David’s card is legit!
//
//  So, validating credit card numbers isn’t hard, but it does get a bit tedious by hand. Let’s
//  write a program.

// Requirements
// 1.- In the file called credit.c in the credit directory, write a program that prompts the user
// for
//     a credit card number and then reports (via printf) whether it is a valid American Express,
//     MasterCard, or Visa card number, per the definitions of each’s format herein. So that we can
//     automate some tests of your code, we ask that your program’s last line of output be AMEX\n or
//     MASTERCARD\n or VISA\n or INVALID\n, nothing more, nothing less. For simplicity, you may
//     assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be
//     printed on an actual card) and that it won’t have leading zeroes. But do not assume that the
//     user’s input will fit in an int! Best to use get_long from CS50’s library to get users’
//     input. (Why?)
//
// 2.- Consider the below representative of how your own program should behave when passed a valid
// credit
//     card number (sans hyphens).
//
//              $ ./credit
//              Number: 4003600000000014
//              VISA
//
// 3.- Now, get_long itself will reject hyphens (and more) anyway:
//
//              $ ./credit
//              Number: 4003-6000-0000-0014
//              Number: foo
//              Number: 4003600000000014
//              VISA
//
// 4.- But it’s up to you to catch inputs that are not credit card numbers (e.g., a phone number),
// even
//     if numeric:
//
//              $ ./credit
//              Number: 6176292929
//              INVALID
//
// 5.- Test out your program with a whole bunch of inputs, both valid and invalid. (We certainly
// will!) Here are a few card numbers that PayPal recommends for testing.
//
//              American Express	            371387838021022
//              American Express	            371449635398431
//              American Express                371387838021022
//              American Express Corporate	    378734493671000
//
//              Diners Club	                    30569309025904
//
//              Discover	                    6011111111111117
//              Discover	                    6011000990139424
//
//              JCB	                            3530111333300000
//              JCB	                            3566002020360505
//
//              Mastercard	                    2221000000000009
//              Mastercard	                    2223000048400011
//              Mastercard	                    2223016768739313
//              Mastercard	                    5555555555554444
//              Mastercard	                    5105105105105100
//              Mastercard                      5199999999999991
//              Mastercard                      5299999999999990
//
//              Visa                            4003600000000014
//              Visa	                        4111111111111111
//              Visa	                        4012888888881881
//              Visa	                        4222222222222
//              Visa	                        4999991111111113
//              Visa                            4999992222222229
//
//

// My pseudo code approach:
// 1.- Ask user for a credit card number with "Number: " using get_long
//
// 2.- Validate as follows:
//   2.1.- For American express, the number of digits must be 15 and the first two digits must be
//         either 34 or 37.  printf AMEX\n if valid or INVALID\n if not
//   2.2.- For Mastercard, the number of digits is 16 and the first two digits are 51, 52, 53, 54,
//         or 55 printf MASTERCARD\n if valid or INVALID\n if not
//   2.3.- For Visa, the number of digits is either 13 or 16.  In addition, the first digit is must
//         be a 4, printf VISA\n if valid or INVALID\n if invalid
//

#include <cs50.h>
#include <stdio.h>

long get_last_digit(long ccNumber);
int get_sum(int num);
string all_checks(long tempNumber);

int main(void)
{
    long ccNumber = 0;
    do
    {
        ccNumber = get_long("Number: ");
    }
    while (ccNumber <= 0);
    // printf("You entered %ld\n", ccNumber);

    long tempNumber = ccNumber;

    string response = all_checks(tempNumber);
    printf("%s\n", response);

    // Confirm if it is Amex.  Need to be 15 digits and the first two must be 34 or 37
}

string all_checks(long tempNumber)
{

    // Get the last digit
    int last_1 = -1, last_2 = -1, last_3 = -1, last_4 = -1, last_5 = -1, last_6 = -1, last_7 = -1;
    int last_8 = -1, last_9 = -1, last_10 = -1, last_11 = -1, last_12 = -1, last_13 = -1;
    int last_14 = -1, last_15 = -1, last_16 = -1;

    last_1 = get_last_digit(tempNumber);
    // printf("last_1 is %i\n", last_1);

    tempNumber = (tempNumber - last_1) / 10;
    if (tempNumber > 0)
    {
        last_2 = get_last_digit(tempNumber);
        // printf("last_2 is %i\n", last_2);
    }

    tempNumber = (tempNumber - last_2) / 10;
    if (tempNumber > 0)
    {
        last_3 = get_last_digit(tempNumber);
        // printf("last_3 is %i\n", last_3);
    }

    tempNumber = (tempNumber - last_3) / 10;
    if (tempNumber > 0)
    {
        last_4 = get_last_digit(tempNumber);
        // printf("last_4 is %i\n", last_4);
    }

    tempNumber = (tempNumber - last_4) / 10;
    if (tempNumber > 0)
    {
        last_5 = get_last_digit(tempNumber);
        // printf("last_5 is %i\n", last_5);
    }

    tempNumber = (tempNumber - last_5) / 10;
    if (tempNumber > 0)
    {
        last_6 = get_last_digit(tempNumber);
        // printf("last_6 is %i\n", last_6);
    }

    tempNumber = (tempNumber - last_6) / 10;
    if (tempNumber > 0)
    {
        last_7 = get_last_digit(tempNumber);
        // printf("last_7 is %i\n", last_7);
    }

    tempNumber = (tempNumber - last_7) / 10;
    if (tempNumber > 0)
    {
        last_8 = get_last_digit(tempNumber);
        // printf("last_8 is %i\n", last_8);
    }

    tempNumber = (tempNumber - last_8) / 10;
    if (tempNumber > 0)
    {
        last_9 = get_last_digit(tempNumber);
        // printf("last_9 is %i\n", last_9);
    }

    tempNumber = (tempNumber - last_9) / 10;
    if (tempNumber > 0)
    {
        last_10 = get_last_digit(tempNumber);
        // printf("last_10 is %i\n", last_10);
    }

    tempNumber = (tempNumber - last_10) / 10;
    if (tempNumber > 0)
    {
        last_11 = get_last_digit(tempNumber);
        // printf("last_11 is %i\n", last_11);
    }

    tempNumber = (tempNumber - last_11) / 10;
    if (tempNumber > 0)
    {
        last_12 = get_last_digit(tempNumber);
        // printf("last_12 is %i\n", last_12);
    }

    tempNumber = (tempNumber - last_12) / 10;
    if (tempNumber > 0)
    {
        last_13 = get_last_digit(tempNumber);
        // printf("last_13 is %i\n", last_13);
    }

    tempNumber = (tempNumber - last_13) / 10;
    if (tempNumber > 0)
    {
        last_14 = get_last_digit(tempNumber);
        // printf("last_14 is %i\n", last_14);
    }

    tempNumber = (tempNumber - last_14) / 10;
    if (tempNumber > 0)
    {
        last_15 = get_last_digit(tempNumber);
        // printf("last_15 is %i\n", last_15);
    }

    tempNumber = (tempNumber - last_15) / 10;
    if (tempNumber > 0)
    {
        last_16 = get_last_digit(tempNumber);
        // printf("last_16 is %i\n", last_16);
    }

    int sumCk = get_sum(last_2) + get_sum(last_4) + get_sum(last_6) + get_sum(last_8);
    sumCk = sumCk + get_sum(last_10) + get_sum(last_12) + get_sum(last_14) + get_sum(last_16);
    // printf("Pass one sum is %i\n", sumCk);

    sumCk = sumCk + last_1 + last_3 + last_5 + last_7 + last_9 + last_11;
    if (last_13 != -1)
    {
        sumCk = sumCk + last_13;
    }
    if (last_15 != -1)
    {
        sumCk = sumCk + last_15;
    }
    // printf("Sum of all returned %i\n",sumCk);

    int passOrFail = (int) get_last_digit((long) sumCk);

    // Lets check if is has a minimal of 13 characters.  Cause if it does not at least 13
    // it is not any type of card
    if (passOrFail > 0)
    {
        return "INVALID";
    }

    // printf("Passed sum\n");
    // else
    //{
    // printf("Pass sum\n");
    //}

    // Check to see if it Amex
    // characters, then it is nothing 4003600000000014 or 371387838021022
    // For American express, the number of digits must be 15 and the first two digits must be
    // either 34 or 37.  printf AMEX\n if valid or INVALID\n if not
    if ((last_16 == -1) && (last_15 != -1))
    {
        if ((last_15 == 3) && (last_14 == 4 || last_14 == 7))
        {
            return "AMEX";
        }
    }

    // If not Amex, then it must be either Visa or Mastercard.  For Mastercard, 16 has to be
    // populated and then the other digits must be 51, 52, 53, 54 or 55
    if ((last_16 == 5) && (last_15 > 0 && last_15 < 6))
    {
        return "MASTERCARD";
    }

    // If we are here, it can only be a VISA or nothing else.
    // For Visa, the number of digits is either 13 or 16.  In addition, the first digit is must
    // be a 4, printf VISA\n if valid or INVALID\n if invalid
    // printf("last_16 = %i\n", last_16);
    // printf("last_13 = %i\n", last_13);
    if (last_16 == 4)
    {
        return "VISA";
    }
    if (last_13 == 4)
    {
        return "VISA";
    }

    return "INVALID";
}

long get_last_digit(long num)
{
    return num % 10;
}

int get_sum(int num)
{
    if (num == -1)
    {
        return 0;
    }
    num = num * 2;
    // So if I pass 9 then 9 * 2 = 18 and 1+8 = 9
    // So if I pass 5 then 5 * 2 = 10 and 1+0 = 1
    // So if I pass 6 then 6 * 2 = 12 and 1 + 2 = 3
    if (num > 9)
    {
        num = 1 + (int) get_last_digit((long) num);
        return num;
    }
    else
    {
        return num;
    }
}
