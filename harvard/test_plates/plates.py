"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/12"


# ▓Original requirements
# ░ In Massachusetts, home to Harvard University, it’s possible to request a vanity license
# ░ plate for your car, with your choice of letters and numbers instead of random ones. Among
# ░ the requirements, though, are:
# ░   1.- “All vanity plates must start with at least two letters.”
# ░   2.- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a
# ░       minimum of 2 characters.”
# ░   3.- “Numbers cannot be used in the middle of a plate; they must come at the end. For
# ░       example, AAA222 would be an acceptable … vanity plate; AAA22A would not be
# ░       acceptable. The first number used cannot be a ‘0’.”
# ░   4.- “No periods, spaces, or punctuation marks are allowed.”
# ░
# ░ Implement a program that prompts, with "Plate: ", the user for a vanity plate and then
# ░ output "Valid" if meets all of the requirements or "Invalid" if it does not.
# ░ Assume that any letters in the user’s input will be uppercase. Structure your program
# ░ per the below, wherein is_valid returns True if s meets all requirements and False if
# ░ it does not. Assume that s will be a str.
# ░       def main():
# ░       plate = input("Plate: ")
# ░       if is_valid(plate):
# ░           print("Valid")
# ░       else:
# ░           print("Invalid")
# ░
# ░
# ░       def is_valid(s):
# ░           ...
# ░
# ░       main()
# ░


# ▓ Hints:
# ░ 1.- Recall that a str comes with quite a few methods, per
# ░     docs.python.org/3/library/stdtypes.html#string-methods.
# ░ 2.- Much like a list, a str is a “sequence” (of characters), which means it can be
# ░     “sliced” into shorter strings with syntax like s[i:j]. For instance, if s
# ░     is "CS50", then s[0:2] would be "CS".
# ░


# ▓ Extra work problem statement
# ░ You’re welcome to implement additional functions for is_valid to call (e.g., one
# ░ function per requirement).
# ░
# ░


# ▓ My pseudo code approach:
# ░ 1.- Send a message to the screen "Plate: " and accept a user's input.
# ░ 2.- Send the imputed string, using variable named "plate", to a formula named
# ░     "is_valid()".
# ░     2.1.- Function returns "True" if the string can be used as a plate and "False" if it
# ░           cannot.  Alls the checks will be done by formulas themselves.
# ░ 3.- Function above calls a separate function for each validation.  As follows:
# ░     3.1.- Function "strt_w2_lttrs()" that accepts a string and checks to make sure that
# ░           the first two characters are letters.  If it passes return "True" or "False"
# ░           if it does not.
# ░     3.2.- Function "char_len()", that accepts a string, which returns True if the length
# ░           of the string is between 2 and 6.
# ░     3.3.- Function "has_nbr()", that accepts a string, which checks for numbers.  Numbers
# ░           can only start as the thirds character and the rest of the plate cannot contain
# ░           more letters.  If it passes return "True" otherwise return "False"
# ░     3.4.- Function "valid_chars()", that accepts a string, and makes sure that none of the
# ░           characters are periods ".", spaces " " or punctuation marks.  If it does not
# ░           contain any of these characters, return "True" otherwise return "False"
# ░
# ░


# ▓ Revision Requirements:
# ░ Reimplement Vanity Plates from Problem Set 2, restructuring your code per the below,
# ░ wherein is_valid still expects a str as input and returns True if that str meets all
# ░ requirements and False if it does not, but main is only called if the value of
# ░ __name__ is "__main__":
# ░
# ░         def main():
# ░             ...
# ░
# ░
# ░         def is_valid(s):
# ░             ...
# ░
# ░
# ░         if __name__ == "__main__":
# ░             main()
# ░
# ░ Then, in a file called test_plates.py, implement four or more functions that
# ░ collectively test your implementation of is_valid thoroughly, each of whose names
# ░ should begin with test_ so that you can execute your tests with:
# ░
# ░         pytest test_plates.py


# ▓ My revision pseudo code approach:
# ░ 1.-
# ░
# ░
# ░


def strt_w2_lttrs(plate: str) -> bool:
    ''' Function:
            Accepts a string and inspects it to make sure that the first two characters
            are letters.

        Returns:
            True if the first two characters are letters and not numbers or False if they
            are not.
    '''
    # Check only the first two letters
    # if plate[0:2].isalpha():
    #     print('Pass check strt_w2_lttrs(plate)')

#    print(f'The first two characters are {
#          plate[0:2]} and the result is {plate[0:2].isalpha()}')
#    print('Inside strt_w2_lttrs(plate: str)')
    # else:
    #     print('FAIL check strt_w2_lttrs(plate)')
    return plate[0:2].isalpha()


def char_len(plate: str) -> bool:
    ''' Function accepts a string and inspects it to make sure that the string's length is
        between 2 and 6.

        Returns True if it passes condition or False if it does not.
    '''
#    print(f'String length is {len(plate)} and the result is {
#          True if 2 <= len(plate) <= 6 else False}')
#    print('Inside char_len(plate: str)')
    # if 2 <= len(plate) <= 6:
    #     print('Pass check char_len(plate: str)')
    # else:
    #     print('FAIL check char_len(plate: str)')

    return True if 2 <= len(plate) <= 6 else False


def has_nbr(plate: str) -> bool:
    ''' Function accepts a string and inspects it to make sure that if the string has numbers,
        that they start a position 3 and the rest of the string is a number.

        Returns True if it passes condition or False if it does not.
    '''
    # Check every character, after the first two, and see if it is an integer.  It it is,
    # the rest of the string must be integer.
    # Using a variable to understand the start and end of the string that must be tested.
#    print('Inside has_nbr(plate: str)')
    pos = 2
    for letter in plate[2:]:
        #        print('---- Inspecting letter.  Letter is [' + letter + ']')
        #        print('------- The rest of the string is [' + plate[pos:] + ']')
        if letter == '0':
            return False
        if letter.isnumeric():
            if plate[pos:].isnumeric():
                #                print('Pass check has_nbr(plate: str)')
                return True
            else:
             #               print('FAIL check has_nbr(plate: str)')
                return False
        pos += 1
        if pos == 6:
            return True


def valid_chars(plate: str) -> bool:
    ''' Function accepts a string and inspects it to make sure that the string does not contain
        periods ".", spaces " " or any punctuation mark.

        Returns True if it passes condition or False if it does not.
    '''
#    print('Inspecting for punctuations in [' + plate[2:] + ']')
    p_mark = "!#$%&'()*+,-./:;\"<=>?@[\\]^_`{|} ~"
    for letter in plate[2:]:
        if letter in p_mark:
            #            print('Pass check valid_chars(plate: str)')
            return False
        else:
            #            print('FAIL check valid_chars(plate: str)')
            return True


def is_valid(plate: str) -> bool:
    ''' Function accepts a string and will call multiple validator functions, passing the same
        string, to validate if the string passes plate name requirements.

        Returns True if the plate name is valid and false if it is not.
    '''
    if strt_w2_lttrs(plate) and char_len(plate) and has_nbr(plate):  # and valid_chars(plate)
        #        print('Pass MAIN check is_valid(plate: str)')
        return True
    else:
        #        print('FAIL MAIN check is_valid(plate: str)')
        return False


def main():
    my_str = ('Plate: ')
    plate = input(my_str)
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


# Call main only when intended
if __name__ == '__main__':
    main()
