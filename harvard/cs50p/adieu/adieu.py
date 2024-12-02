"""
A eDX assignment.

This file shows how modules work

"""


__author__ = "John Rocha"
__date__ = "2024/09/15"
#;






















# < Original Requirements:
# > The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these
# > lyrics, wherein “adieu” means “goodbye” in French:
# >
# >         Adieu, adieu, to yieu and yieu and yieu
# >
# > Of course, the line isn’t grammatically correct, since it would typically be written(with
# > an Oxford comma) as:
# >
# >         Adieu, adieu, to yieu, yieu, and yieu
# >
# > To be fair, “yieu” isn’t even a word it just rhymes with “you”!
# >
# > Implement a program that prompts the user for names, one per line, until the user inputs
# > control-d. Assume that the user will input at least one name. Then bid adieu to those
# > names, separating two names with one and, three names with two commas and one and, and
# > "n" names with "n - 1" commas and one and, as in the below:
# >         Adieu, adieu, to Liesl
# >         Adieu, adieu, to Liesl and Friedrich
# >         Adieu, adieu, to Liesl, Friedrich, and Louisa
# >         Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# >         Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# >         Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# >         Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
# >

# < Hints:
# > Note that the inflect module comes with quite a few methods, per
# > pypi.org/project/inflect. You can install it with:
# >         pip install inflect
# >
# > Note than the documentation for inflect is itself a bit buggy because join is a
# > method, it should be called like "p.join(...)" and not "join(...)".
# >

# < Extra work requirements:
# > None defined
# >

# < My pseudo code approach:
# > 1.- Install inflect in the Anaconda "Train1" environment.
# > 2.- Import into your program library inflect and follow instructions on how to
# >     instantiate and use it.
# > 3.- Ask user, with message "Name: ", to enter names.  Continue to ask for names
# >     until the user breaks out of entering names
# > 4.- Using the inflect's join function, produce the output as the specs call for
# >

#<

import inflect

p = inflect.engine()


def get_names() -> list:
    """
    get_names
    Function returns a list of names imputed which the user enters

    The function will prompt the user with "Name: " and then:
    1.- If the user does not enter any characters, ask again.
    2.- If the user enters a valid string, add the string to a local list
    3.- If the user enters control-d, exist the loop and return the list

    Returns:
        Returns a list of strings where each element is a name.
    """
    nm_lst = list()
    while True:
        try:
            resp = input('Name: ').strip()
            nm_lst.append(resp)
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            break
    return nm_lst


def main():
    # * Get the names from the user
    name_lst = list()
    name_lst = get_names()
    out_msg = p.join(name_lst)

    # | This line below was problematic.  Unless I returned the results of the p.join() to a variable,
    # | the output would not pass.
    # //print(f'Adieu, adieu, to {out_msg}')
    print(f'Adieu, adieu, to {p.join(name_lst)}')


# * Call main only when intended
if __name__ == "__main__":
    main()
