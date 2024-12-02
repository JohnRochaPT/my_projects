"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/10"


# Original Requirements
# Write a In a program called playback.py that prompts the user for input and then
# outputs that same input, replacing each "space" with three periods "..."

# Extra work problem statement
# None defined

# Get the string from the user
getStr = input('Speak to me please: \n')

# Replace spaces with three periods "..."
newStr = getStr.replace(' ', '...')

# Return the string back with spaces replaced with three periods
print(newStr)
