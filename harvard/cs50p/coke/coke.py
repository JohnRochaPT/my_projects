"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/11"


# Original requirements
# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins
# in these denominations: 25 cents, 10 cents, and 5 cents.
#
# Implement a program that prompts the user to insert a coin, one at a time, each time informing
# the user of the amount due. Once the user has inputted at least 50 cents, output how many
# cents in change the user is owed. Assume that the user will only input integers, and
# ignore any integer that isn’t an accepted denomination.
#
# Extra work problem statement
# None defined
#
# My pseudo code approach:
#   1.- Create a variable to track amount due
#   2.- Define a function to calculate paid amount.  Call function "add_coin".
#   3.- Create a while True loop
#       3.1.- Print to the screen the amount due "Amount Due: " and disclose the amount that is
#             due. At the beginning the due amount will be 50
#       3.2.- Prompt the user to insert a coin with message "Insert Coin :"
#       3.3.- If the user enters anything other than 20, 15 or 5, restart the loop
#       3.4.- If the amount is accepted, deduct the amount from the amount due and:
#           3.4.1.- If the amount due is zero, end the program with "Change Owed: 0"
#           3.4.2.- If the amount due is > zero, print "Amount Due: " with the new due amount
#                   and ask to insert another coin.
#           3.4.3.- If the user has over paid, print "Change Owed: " and disclose the change
#                   due amount.
#

def add_coin() -> int:
    '''  Function asks user to insert a coin.  The coin is only accepted if it is 25, 10 or
         5.  If the coin is valid, return the coin value otherwise return 0
    '''
    ret_val = int(input('Insert Coin: '))
    match ret_val:
        case 25:
            return 25
        case 10:
            return 10
        case 5:
            return 5
        case _:
            return 0


def main():
    amt_due = 50
    first_mg = 'Amount Due: '
    second_mg = 'Insert Coin:'
    while amt_due > 0:
        # Ask to insert a new coin
        print(f'Amount Due: {amt_due}')
        amt_due = amt_due - add_coin()
        if amt_due <= 0:
            print('Change Owed:', amt_due * -1)


# Call main only when intended
if __name__ == '__main__':
    main()
