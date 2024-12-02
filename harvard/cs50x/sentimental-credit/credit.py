"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/10/25'
__contact__ = 'john.rocha@outlook.com'
__version__ = '0.0.1'
__credits__ = 'Something'

#++************************************************************************************************
#+ User Story:
#++************************************************************************************************
#; A credit (or debit) card, of course, is a plastic card with which you can pay for goods and
#; services. Printed on that card is a number that’s also stored in a database somewhere, so that
#; when your card is used to buy something, the creditor knows whom to bill. There are a lot of
#; people with credit cards in this world, so those numbers are pretty long: American Express uses
#; 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. And
#; those are decimal numbers (0 through 9), not binary, which means, for instance, that American
#; Express could print as many as 10^15 = 1,000,000,000,000,000 unique cards! (That’s, um, a
#; quadrillion.)
#;
#; Actually, that’s a bit of an exaggeration, because credit card numbers actually have some
#; structure to them. All American Express numbers start with 34 or 37; most MasterCard numbers
#; start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we
#; won’t concern ourselves with for this problem); and all Visa numbers start with 4. But credit
#; card numbers also have a “checksum” built into them, a mathematical relationship between at
#; least one number and others. That checksum enables computers (or humans who like math) to
#; detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a
#; database, which can be slow. Of course, a dishonest mathematician could certainly craft a fake
#; number that nonetheless respects the mathematical constraint, so a database lookup is still
#; necessary for more rigorous checks.
#;
#; In a file called credit.c in a folder called credit, implement a program in C that checks the
#; validity of a given credit card number.
#;
#; Need to accept at least 13- and 16-digit numbers
#;
#;


#++************************************************************************************************
#+ Luhn’s Algorithm:
#+*************************************************************************************************
#; So what’s the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of
#; IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically)
#; valid as follows:
#;
#;    1.- Multiply every other digit by 2, starting with the number’s second-to-last digit, and
#;        then add those products’ digits together.
#;
#;    2.- Add the sum to the sum of the digits that weren’t multiplied by 2.
#;
#;    3.- If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is
#;        congruent to 0), the number is valid!
#;
#; That’s kind of confusing, so let’s try an example with David’s Visa: 4003600000000014.
#;
#;    1.- For the sake of discussion, let’s first put in parenthesis every other digit, starting
#;        with the number’s second-to-last digit:
#;
#>                      (4)0(0)3(6)0(0)0(0)0(0)0(0)0(1)4
#>                       4   0   6   0   0   0   0   1
#;
#;        Okay, let’s multiply each of the underlined digits by 2:
#;
#>                      1*2 + 0*2 + 0*2 + 0*2 + 0*2 + 6*2 + 0*2 + 4*2
#;
#;        That gives us:
#;
#>                      2 + 0 + 0 + 0 + 0 + 12 + 0 + 8
#;
#;        Now let’s add those products’ digits (i.e., not the products themselves) together:
#;
#>                      2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
#;
#;    2.- Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2
#;        (starting from the end):
#;
#>                      13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20
#;
#;    3.- Yup, the last digit in that sum (20) is a 0, so David’s card is legit!
#;
#; So, validating credit card numbers isn’t hard, but it does get a bit tedious by hand. Let’s
#; write a program.
#;
#;


#++************************************************************************************************
#+ Implementation Details:
#++************************************************************************************************
#; 1.- So that we can automate some tests of your code, we ask that your program’s last line of
#;     output be AMEX\n or MASTERCARD\n or VISA\n or INVALID\n, nothing more, nothing less.
#;
#; 2.- For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid
#;     of hyphens, as might be printed on an actual card).
#;
#; 3.- Best to use get_int or get_string from CS50’s library to get users’ input, depending on how
#;     you to decide to implement this one.
#;
#;

import re


#++************************************************************************************************
#+  **********************           C L A S S    S E C T I O N            ************************
#++************************************************************************************************
class Kit():
    """
    MyKit
        Class contains class methods that are used as workhorses to perform functions that I use
        often
    """

    @staticmethod
    def get_str_input(msg: str) -> str:
        """
        get_str_input
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user must input at least one character.  If the input is not valid, it will
            keep asking for an input.

        Arguments:
            msg -- A string.  Can be an empty string.

        Returns:
            Returns a string of at least one character
        """
        while True:
            response = input(msg).strip()
            if len(response) == 0:
                pass
            else:
                return response

    @staticmethod
    def get_str_input_even_empty(msg: str) -> str:
        """
        get_str_input_even_empty
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user can choose to enter something or nothing, by hitting enter.  The
            function allows for empty strings

        Arguments:
            msg -- A string.  Can be an empty string.

        Returns:
            Returns a string.  Can be a string of zero length
        """
        return input(msg).strip()

    @staticmethod
    def get_pos_int_input(msg: str) -> str:
        """
        get_pos_int_input
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user must enter at least one positive integer.  If the input is not
            valid, it will keep asking for an input until the user enters a valid integer.

        Arguments:
            msg -- A string.  Can be empty string.

        Returns:
            Returns an integer.
        """
        while True:
            try:
                response = input(msg).strip()
                if '.' in response:
                    pass
                else:
                    response = int(response)
                    return response
            except:
                pass

    @staticmethod
    def get_pos_flt_input(msg: str) -> str:
        """
        get_pos_int_input
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user must enter a positive float.  If the input is not valid, it will
            keep asking for an input until the user enters a valid integer.

        Arguments:
            msg -- A string.  Can be empty string.

        Returns:
            Returns an float.
        """
        while True:
            try:
                response = input(msg).strip()
                if '.' in response:
                    response = float(response)
                    return response
                else:
                    pass
            except:
                pass

    @staticmethod
    def lines():
        """
         lines
            Function prints a separator section to make it easier to read when looking at the
            terminal window.  Use it instead of multiple print() lines
        """
        name = __file__.split('\\')[len(__file__.split('\\'))-1]
        stars = int(((80-len(name))/2))
        line = '\n' * 6 + '=' * stars + ' ' * 5 + name + ' ' * 5 + '=' * stars + '\n'
        print(line, end='')

    @staticmethod
    def format_validator(str_to_validate: str, pattern_cd: str) -> re.Match:
        """
        format_validator
            Function facilitates the validating of strings against certain formats.

            Function uses the "re" library to perform regular expression matches.  If the
            contents of the string matches the pattern, it returns True.  If there is no
            match, it returns false.  When calling this function send the string to be
            validated and the following codes for specialized formats:

                "zip" when validating the format for zip codes
                "phone" when validating a phone number
                "date" when validating YYYY-MM-DD for dates
                "SSN" when validating Social Security Numbers

        Arguments:
            str_to_validate -- Non empty string to use matched against a pattern
            pattern_cd -- Regular expression pattern.

        Returns:
            Returns a re.Match object.  Either empty or not.  If not empty, there
            was a match
        """
        match pattern_cd:
            case 'zip':
                pattern = r'^[0-9]{5}$'
            case 'phone':
                pattern = r'^[0-9](-|.| )[0-9]{3}(-|.| )[0-9]{3}(-|.| )[0-9]{4}$'
            case 'date':
                pattern = r'^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$'
            case 'ssn':
                pattern = r'^[0-9]{3}-[0-9]{2}-[0-9]{4}$'

        return re.search(pattern, str_to_validate, re.IGNORECASE)


#++************************************************************************************************
#+  **********************    M A I N    P R O G R A M    S E C T I O N    ************************
#++************************************************************************************************

def main():
    # > This is an inline code comment.

    #; Get 13 to 16 digits
    pattern = r'^[0-9]{1,16}$'
    while (True):
        cc_number = Kit.get_str_input("Number: ")
        match = re.search(pattern, cc_number, re.IGNORECASE)
        if (not match):
            continue
        else:
            break

    #; Multiply every other number, starting from right to left, and then sum them together
    #; however, if the multiplication by 2 results in more than one digit, we need to return
    #; the sum of those digits
    length = len(cc_number)
    if (length < 13):
        print("INVALID")
        return

    every_other = (get_sum(cc_number[length - 2]) +
                   get_sum(cc_number[length - 4]) +
                   get_sum(cc_number[length - 6]) +
                   get_sum(cc_number[length - 8]) +
                   get_sum(cc_number[length - 10]) +
                   get_sum(cc_number[length - 12]) )

    if (length > 13 and length < 16):
        every_other = every_other + get_sum(cc_number[length - 14])

    if (length == 16):
        every_other = every_other + (get_sum(cc_number[length - 14]) +
                                     get_sum(cc_number[length - 16]) )

    #< print(f"The length of the card is {length}")
    #< print(f"The sum of every other multiplication digits is [{every_other}]")

    #; Now we need to add every other number we did not include
    other_digits = (int(cc_number[length - 1]) +
                    int(cc_number[length - 3]) +
                    int(cc_number[length - 5]) +
                    int(cc_number[length - 7]) +
                    int(cc_number[length - 9]) +
                    int(cc_number[length - 11]) )

    if (length <= 16):
        other_digits = (other_digits +
                        (int(cc_number[length - 13]) +
                         int(cc_number[length - 15])))

    #< print(f"The sum of the other numbers [{other_digits}]")

    digits = every_other + other_digits

    #< print(f"The sum of the all the numbers [{digits}]")

    if (str(digits)[1] == "0"):
        pass
    else:
        print("Sum INVALID")


    card_type = what_card(cc_number)
    print(card_type)
    return

#
#
#
#++************************************************************************************************
#+  **************************    F U N C T I O N     S E C T I O N    ****************************
#++************************************************************************************************


def what_card(cc_number: str) -> str:
    """
    what_card
        Function accepts a string and determines what type of card is it.  It then returns a string
        with the type of card

    Arguments
        cc_number -- A string with the credit card number

    Returns
        Returns a string with the type of credit card.  It returns "AMEX", "MASTERCARD", "VISA"
        or "INVALID"
    """

    cc_len = len(cc_number)
    #; American express are 15 characters long and start with 34 or 37
    if (cc_len == 15 and cc_number[0] == "3" and cc_number[1] in ["4","7"]):
        return "AMEX"

    #; Mastercard numbers are 16 digits long and must start with 51, 52, 53, 54 or 55
    if (cc_len == 16 and cc_number[0] == "5" and cc_number[1] in ["1","2","3","4","5"]):
        return "MASTERCARD"

    #; Visa numbers are either 13 or 16 digits and it must start with 4
    if((cc_len == 13 or cc_len == 16) and cc_number[0] == "4"):
        return "VISA"
    else:
        return "INVALID"


def get_sum(number: str) -> int:
    """
    get_sum
        Function accepts a string between 0 and 9 and if the multiplication of that number results
        in less than two digits, it will return that digit.  If the multiplication results in a
        number greater than 10, it will return the addition of those two digits

    Arguments:
        number -- An integer between 0 and 9

    Returns:
        Returns an integer
    """
    if (int(number) <= 4):
        return int(number) * 2
    else:
        return int(number) * 2 - 10 + 1

#
#
#
#
#++************************************************************************************************
#+  **********************           C A L L   S E L F   M A I N           ************************
#++************************************************************************************************
# > Call main ONLY when intended
if __name__ == '__main__':
    main()

