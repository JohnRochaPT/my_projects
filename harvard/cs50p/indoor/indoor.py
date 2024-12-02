"""
A program that takes an input and returns the input in lower case

Author: John Rocha
Date: 09/09/2024
"""
# Original Requirements:
# The request is to ask the user, using function "input()", to enter something in the
# screen.  That could be one word or many.  Then we are supposed to convert the entire
# string into all lowercase letters.  Punctuation and whitespace should be outputted
# unchanged.
# 1.- Ask the user to input a string.  No limit of length
# 2.- Prompt the user, by passing a str to the "input()" function, to enter words in
#     the screen.
# 3.- Send to the screen, the entire string converted to all lowercase letters

# Get string from user
getString = input(
    "Please tell me something.  When done, hit the enter key: \n")

# Convert the string to all lowercase
getString = getString.lower()

# Print to the screen the new text
print(getString)

