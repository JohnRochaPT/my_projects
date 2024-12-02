"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/11"


# Original Requirements
# Implement a program that prompts the user for the name of a file and then outputs that file’s
# media type if the file’s name ends, case-insensitively, in any of these suffixes:
#   .gif        maps to:    image/gif
#   .jpg        maps to:    image/jpeg
#   .jpeg       maps to:    image/jpeg
#   .png        maps to:    image/png
#   .pdf        maps to:    application/pdf
#   .txt        maps to:    text/plain
#   .zip        maps to:    application/zip
# If the file’s name ends with some other suffix or has no suffix at all, output
# "application/octet-stream" instead, which is a common default.


# Extra work problem statement
# Not defined

# My pseudo code approach:
#   1.- Prompt user to enter a file name.  Ask "File Name: "
#   2.- Ignore case of the input string.  You do not need to check to make sure the string has
#       the correct format.
#   3.- If the user's response matches any of the file extensions, defined in the "Original
#       Requirements", print out the matched, or "maps to:", media type.
#

def main():
    myStr = 'File Name: '
    respStr = input(myStr).strip().lower()

    # Get the file extension
    fileExt = respStr[respStr.rfind('.'):]
    # print('Period is in: ', fileExt)

    # Match the extension
    match fileExt:
        case '.gif':
            print('image/gif')
        case '.jpg' | '.jpeg':
            print('image/jpeg')
        case '.png':
            print('image/png')
        case '.pdf':
            print('application/pdf')
        case '.txt':
            print('text/plain')
        case '.zip':
            print('application/zip')
        case _:
            print('application/octet-stream')


main()
