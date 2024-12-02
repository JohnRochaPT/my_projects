"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/18'

# .Original Requirements:
#: After finishing CS50 itself, students on campus at Harvard traditionally receive their very
#: own I took CS50 t-shirt. No need to buy one online, but like to try one on virtually?
#:
#: Implement a program that expects exactly two command-line arguments:
#:   1.- In sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
#:
#:   2.- In sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
#:
#:
#: The program should then overlay shirt.png (which has a transparent background) on the input
#: after resizing and cropping the input to be the same size, saving the result as its output.
#:
#: Open the input with Image.open, per
#: pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the
#: input with ImageOps.fit, per
#: pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default
#: values for method, bleed, and centering, overlay the shirt with Image.paste, per
#: pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the
#: result with Image.save, per
#: pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.
#:
#: The program should instead exit via sys.exit:
#:   1.- If the user does not specify exactly two command-line arguments,
#:   2.- If the input’s and output’s names do not end in .jpg, .jpeg, or .png,
#:       case-insensitively,
#:   3.- If the input’s name does not have the same extension as the output’s name, or
#:   4.- If the specified input does not exist.
#:
#: Assume that the input will be a photo of someone posing in just the right way, like these
#: demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
#:
#:
#: If you’d like to run your program on a photo of yourself, first drag the photo over to
#: VS Code’s file explorer, into the same folder as shirt.py. No need to submit any photos
#: with your code. But, if you would like, you’re welcome (but not expected) to share a photo
#: of yourself wearing your virtual shirt in any of CS50’s communities!
#:


# .Hints:
#: 1.- Note that you can determine a file’s extension with os.path.splitext, per
#:     docs.python.org/3/library/os.path.html#os.path.splitext.
#:
#: 2.- Note that open can raise a FileNotFoundError, per
#:     docs.python.org/3/library/exceptions.html#FileNotFoundError.
#:
#: 3.- Note that the Pillow package comes with quite a few classes and methods, per
#:     pypi.org/project/Pillow. You might find its handbook and reference helpful to skim. You
#:     can install the package with:
#:
#:                  pip install Pillow
#:
#:          - You can open an image (e.g., shirt.png) with code like:
#:
#:                  shirt = Image.open("shirt.png")
#:
#:          - You can get the width and height, respectively, of that image as a tuple with code
#:            like:
#:
#:                  size = shirt.size
#:
#:          - And you can overlay that image on top of another (e.g., photo) with code like
#:
#:                  photo.paste(shirt, shirt)
#:
#:          - Wherein the first shirt represents the image to overlay and the second shirt
#:            represents a “mask” indicating which pixels in photo to update.
#:
#:  4.- Note that you can open an image (e.g., shirt.png) in VS Code by running
#:
#:                  code shirt.png
#:
#:          - Or by double-clicking its icon in VS Code’s file explorer.
#:
#:


# .Extra work requirements:
#: None defined
#:


# .My pseudo code approach:
#: 1.- Import sys library to handle input argument errors.  In addition, import Pillow.  If
#:     Pillow does not resolve, install it.
#:
#: 2.- Program requires two arguments. The first argument represents the "input" file and
#:     the second argument is the "output" file.  Reuse code from the "scourgify.py"
#:     program.  Reject the user's input if:
#:   2.1.- Reject the execution if the user passes less than 3 arguments, whereas the first
#:         argument is the program name.
#:   2.2.- Reject the execution if the user passes more than 3 arguments.
#:   2.3.- If the input’s and output’s names do not end in .jpg, .jpeg, or .png,
#:         case-insensitively,
#:   2.4.- If the input’s name does not have the same extension as the output’s name
#:   2.3.- If the specified input file does not exist.
#:
#: 3.- Obtain the size parameters for file "shirt.pgn".  This file has a transparent
#:     background and will be the file that will be used to overlay the first file (used
#:     as input)
#:
#: 4.- Resize the input file to match the shirt.pgn file and then overlay shirt.pgn over
#:     the first file and save it as the second file (used as output).  Do not modify the
#:     first file.
#:   4.1.- The size of the input files is 1200 x 1600
#:


import sys
from PIL import Image, ImageOps


def check_args() -> bool:
    """
    check_args
        Function checks that the user passed valid file names when launching this program

        Conditions:
            1.- There can only be three arguments. The program name, the first file name and
                the second file name.  If there are less than three arguments or more than
                three, exist with sys.exit()
            2.- If the file names does not end with "*.csv", exist with sys.exit()
            3.- If the second file does not exist end with sys.exit()

    Returns:
        Returns True if all conditions are met.
    """
    # > If there is less than 3 argument
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    # > If there are more than 3 arguments, there are too many
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    # > Check the extension of the files.
    ext1 = sys.argv[1].strip().split('.')[1]
    ext2 = sys.argv[2].strip().split('.')[1]
    if ext1 not in ('png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', '.png', '.PNG', '.jpg', '.JPG'):
        sys.exit(f'Could not read {sys.argv[1]}')

    if ext2 not in ('png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', '.png', '.PNG', '.jpg', '.JPG'):
        sys.exit(f'Could not read {sys.argv[2]}')

    if ext1 != ext2:
        sys.exit('File extensions are not the same.')

    # > Now we need to determine if we can open the file
    try:
        shirt = Image.open(sys.argv[1])
        shirt.close()
        return True
    except:
        sys.exit('File does not exists')
        return False


def overlay_size() -> tuple:
    """
    overlay_size
        Function opens the overlay file and gets the size attributes.

    Returns:
        Function returns a tuple with the dimensions for the overlay file.
    """
    with Image.open('shirt.png') as overlay_image:
        # > image.size returns a tuple that is width by heigh in pixels.
        size = overlay_image.size
        # > The size is 600 pixels wide and 600 pixels tall
        return size


def main():
    # > This is an inline code comment.
    if check_args():
        pass

    # > Get the size of the overlaying image
    size = tuple()
    size = overlay_size()

    # > The overlaying file size is 600x600.
    # > Resize as close as possible first.
    overlay_im = Image.open('shirt.png')
    with Image.open(sys.argv[1]) as original_im:
        # > The below statement forces the image to resize and crop to the overlaying image
        input_cropped = ImageOps.fit(original_im, size)
        # > Now we can overlay them
        input_cropped.paste(overlay_im, mask=overlay_im)
        input_cropped.save(sys.argv[2])

    # shirt = Image.open('shirt.png')
    # with Image.open(sys.argv[1]) as input:
    #     input_cropped = ImageOps.fit(input, shirt.size)
    #     input_cropped.paste(shirt, mask=shirt)
    #     input_cropped.save(sys.argv[2])
# > Call main ONLY when intended
if __name__ == '__main__':
    main()
