//+*************************************************************************************************
//+ Problem to Solve:
//+*************************************************************************************************
//: Perhaps the simplest way to represent an image is with a grid of pixels (i.e., dots), each of
//: which can be of a different color. For black-and-white images, we thus need 1 bit per pixel, as
//: 0 could represent black and 1 could represent white, as in the below.
//:
//: In this sense, then, is an image just a bitmap (i.e., a map of bits). For more colorful images,
//: you simply need more bits per pixel. A file format (like BMP, JPEG, or PNG) that supports
//: “24-bit color” uses 24 bits per pixel. (BMP actually supports 1-, 4-, 8-, 16-, 24-, and 32-bit
//: color.)
//:
//: A 24-bit BMP uses 8 bits to signify the amount of red in a pixel’s color, 8 bits to signify the
//: amount of green in a pixel’s color, and 8 bits to signify the amount of blue in a pixel’s
//: color. If you’ve ever heard of RGB color, well, there you have it: red, green, blue.
//:
//: If the R, G, and B values of some pixel in a BMP are, say, 0xff, 0x00, and 0x00 in hexadecimal,
//: that pixel is purely red, as 0xff (otherwise known as 255 in decimal) implies “a lot of red,”
//: while 0x00 and 0x00 imply “no green” and “no blue,” respectively. In this problem, you’ll
//: manipulate these R, G, and B values of individual pixels, ultimately creating your very own
//: image filters.
//:
//: In a file called helpers.c in a folder called filter-less, write a program to apply filters to
//: BMPs.
//:
//: Usage:
//:
//>         $ ./filter -g ./images/courtyard.bmp ./images/courtyard-grayscale.bmp
//>         $ ./filter -s ./images/stadium.bmp ./images/stadium-sepia.bmp
//>         $ ./filter -r ./images/tower.bmp ./images/tower-reflected.bmp
//>         $ ./filter -b ./images/yard.bmp ./images/yard-blurred.bmp

//+*************************************************************************************************
//+ Background:  A Bit(map) More Technical
//+*************************************************************************************************
//: Recall that a file is just a sequence of bits, arranged in some fashion. A 24-bit BMP file, then,
//: is essentially just a sequence of bits, (almost) every 24 of which happen to represent some
//: pixel’s color. But a BMP file also contains some “metadata,” information like an image’s height
//: and width. That metadata is stored at the beginning of the file in the form of two data
//: structures generally referred to as “headers,” not to be confused with C’s header files.
//: (Incidentally, these headers have evolved over time. This problem uses the latest version of
//: Microsoft’s BMP format, 4.0, which debuted with Windows 95.)
//:
//: The first of these headers, called BITMAPFILEHEADER, is 14 bytes long. (Recall that 1 byte
//: equals 8 bits.) The second of these headers, called BITMAPINFOHEADER, is 40 bytes long.
//: Immediately following these headers is the actual bitmap: an array of bytes, triples of which
//: represent a pixel’s color. However, BMP stores these triples backwards (i.e., as BGR), with 8
//: bits for blue, followed by 8 bits for green, followed by 8 bits for red. (Some BMPs also store
//: the entire bitmap backwards, with an image’s top row at the end of the BMP file. But we’ve
//: stored this problem set’s BMPs as described herein, with each bitmap’s top row first and bottom
//: row last.) In other words, were we to convert the 1-bit smiley above to a 24-bit smiley,
//: substituting red for black, a 24-bit BMP would store this bitmap as follows, where 0000ff
//: signifies red and ffffff signifies white; we’ve highlighted in red all instances of 0000ff.
//:
//: Because we’ve presented these bits from left to right, top to bottom, in 8 columns, you can
//: actually see the red smiley if you take a step back.
//:
//: To be clear, recall that a hexadecimal digit represents 4 bits. Accordingly, ffffff in
//: hexadecimal actually signifies 111111111111111111111111 in binary.
//:
//: Notice that you could represent a bitmap as a 2-dimensional array of pixels: where the image
//: is an array of rows, each row is an array of pixels. Indeed, that’s how we’ve chosen to
//: represent bitmap images in this problem.
//:

//+*************************************************************************************************
//+ Image Filtering:
//+*************************************************************************************************
//: What does it even mean to filter an image? You can think of filtering an image as taking the
//: pixels of some original image, and modifying each pixel in such a way that a particular effect
//: is apparent in the resulting image.
//:
//:
//+ Understanding
//: Let’s now take a look at some of the files provided to you as distribution code to get an
//: understanding for what’s inside of them.
//:
//:
//+ bmp.h
//: Open up bmp.h (as by double-clicking on it in the file browser) and have a look.
//:
//: You’ll see definitions of the headers we’ve mentioned (BITMAPINFOHEADER and BITMAPFILEHEADER).
//: In addition, that file defines BYTE, DWORD, LONG, and WORD, data types normally found in the
//: world of Windows programming. Notice how they’re just aliases for primitives with which you are
//: (hopefully) already familiar. It appears that BITMAPFILEHEADER and BITMAPINFOHEADER make use of
//: these types.
//:
//: Perhaps most importantly for you, this file also defines a struct called RGBTRIPLE that, quite
//: simply, “encapsulates” three bytes: one blue, one green, and one red (the order, recall, in
//: which we expect to find RGB triples actually on disk).
//:
//: Why are these structs useful? Well, recall that a file is just a sequence of bytes (or,
//: ultimately, bits) on disk. But those bytes are generally ordered in such a way that the first
//: few represent something, the next few represent something else, and so on. “File formats”
//: exist because the world has standardized what bytes mean what. Now, we could just read a file
//: from disk into RAM as one big array of bytes. And we could just remember that the byte at
//: array[i] represents one thing, while the byte at array[j] represents another. But why not give
//: some of those bytes names so that we can retrieve them from memory more easily? That’s
//: precisely what the structs in bmp.h allow us to do. Rather than think of some file as one long
//: sequence of bytes, we can instead think of it as a sequence of structs.
//:
//:
//+ filter.c
//: Now, let’s open up filter.c. This file has been written already for you, but there are a couple
//: important points worth noting here.
//:
//: First, notice the definition of filters on line 10. That string tells the program what the
//: allowable command-line arguments to the program are: b, g, r, and s. Each of them specifies a
//: different filter that we might apply to our images: blur, grayscale, reflection, and sepia.
//:
//: The next several lines open up an image file, make sure it’s indeed a BMP file, and read all of
//: the pixel information into a 2D array called image.
//:
//: Scroll down to the switch statement that begins on line 101. Notice that, depending on what
//: filter we’ve chosen, a different function is called: if the user chooses filter b, the program
//: calls the blur function; if g, then grayscale is called; if r, then reflect is called; and if
//: s, then sepia is called. Notice, too, that each of these functions take as arguments the height
//: of the image, the width of the image, and the 2D array of pixels.
//:
//: These are the functions you’ll (soon!) implement. As you might imagine, the goal is for each of
//: these functions to edit the 2D array of pixels in such a way that the desired filter is applied
//: to the image.
//:
//: The remaining lines of the program take the resulting image and write them out to a new image
//: file.
//:
//:
//+ helpers.h
//: Next, take a look at helpers.h. This file is quite short, and just provides the function
//: prototypes for the functions you saw earlier.
//:
//: Here, take note of the fact that each function takes a 2D array called image as an argument,
//: where image is an array of height many rows, and each row is itself another array of width
//: many RGBTRIPLEs. So if image represents the whole picture, then image[0] represents the first
//: row, and image[0][0] represents the pixel in the upper-left corner of the image.
//:
//:
//+ helpers.c
//: Now, open up helpers.c. Here’s where the implementation of the functions declared in helpers.h
//: belong. But note that, right now, the implementations are missing! This part is up to you.
//:
//:
//+ Makefile
//: Finally, let’s look at Makefile. This file specifies what should happen when we run a terminal
//: command like make filter. Whereas programs you may have written before were confined to just
//: one file, filter seems to use multiple files: filter.c and helpers.c. So we’ll need to tell
//: make how to compile this file.
//:
//: Try compiling filter for yourself by going to your terminal and running
//:
//>         $ make filter
//:
//: Then, you can run the program by running:
//:
//>         $ ./filter -g images/yard.bmp out.bmp
//:
//: which takes the image at images/yard.bmp, and generates a new image called out.bmp after
//: running the pixels through the grayscale function. grayscale doesn’t do anything just yet,
//: though, so the output image should look the same as the original yard.
//:
//:

//+*************************************************************************************************
//+ Specification:
//+*************************************************************************************************
//: Implement the functions in helpers.c such that a user can apply grayscale, sepia, reflection, or
//: blur filters to their images.
//:
//:  1.- The function grayscale should take an image and turn it into a black-and-white version of
//:      the same image.
//:
//:  2.- The function sepia should take an image and turn it into a sepia version of the same image.
//:
//:  3.- The reflect function should take an image and reflect it horizontally.
//:
//:  4.- Finally, the blur function should take an image and turn it into a box-blurred version of
//:      the same image.
//:
//: You should not modify any of the function signatures, nor should you modify any other files
//: other than helpers.c.
//:

//+*************************************************************************************************
//+ Implement grayscale
//+*************************************************************************************************
//: One common filter is the “grayscale” filter, where we take an image and want to convert it to
//: black-and-white. How does that work?
//:
//:  1.- Recall that if the red, green, and blue values are all set to 0x00 (hexadecimal for 0),
//:      then the pixel is black. And if all values are set to 0xff (hexadecimal for 255), then the
//:      pixel is white. So long as the red, green, and blue values are all equal, the result will
//:      be varying shades of gray along the black-white spectrum, with higher values meaning
//:      lighter shades (closer to white) and lower values meaning darker shades (closer to black).
//:
//:  2.- So to convert a pixel to grayscale, you just need to make sure the red, green, and blue
//:      values are all the same value. But how do you know what value to make them? Well, it’s
//:      probably reasonable to expect that if the original red, green, and blue values were all
//:      pretty high, then the new value should also be pretty high. And if the original values
//:      were all low, then the new value should also be low.
//:
//:  3.- In fact, to ensure each pixel of the new image still has the same general brightness or
//:      darkness as the old image, you can take the average of the red, green, and blue values to
//:      determine what shade of grey to make the new pixel.
//:
//: If you apply the above algorithm to each pixel in the image, the result will be an image
//: converted to grayscale. Write some pseudocode to help you solve this problem.
//:
//>             void grayscale(int height, int width, RGBTRIPLE image[height][width])
//>             {
//>                 // Loop over all pixels
//>
//>                     // Take average of red, green, and blue
//>
//>                     // Update pixel values
//>             }
//:
//:
//: First, how might you loop over all pixels? Recall that the image’s pixels are stored in the
//: two-dimensional array, image. To iterate over a two-dimensional array, you’ll need two loops,
//: one nested inside the other.
//:
//: Now, you can use image[i][j] to access any individual pixel of the image. But how to take the
//: average of the red, green, and blue elements? Recall each element of image is an RGBTRIPLE,
//: which is the struct defined in bmp.h to represent a pixel. The usual syntax to access members
//: of a struct applies, wherein image[i][j].rgbtRed will give you access to the RGBTRIPLE’s red
//: value, image[i][j].rgbtGreen will give you access to its green value, and so on.
//:
//: When you compute the average, keep in mind the values of a pixel’s rgbtRed, rgbtGreen, and
//: rgbtBlue components are all integers. So be sure to round any floating-point numbers to the
//: nearest integer when assigning them to a pixel value! And why might you want to divide the sum
//: of these integers by 3.0 and not 3?
//:
//: Once you’ve averaged the pixel’s red, green, and blue values into a resulting grayscale color,
//: go ahead and update the pixel’s red, green, and blue values. By now, you’re already acquainted
//: with the syntax for assignment!
//:
//:

//+*************************************************************************************************
//+ Implement sepia
//+*************************************************************************************************
//: Most image editing programs support a “sepia” filter, which gives images an old-timey feel by
//: making the whole image look a bit reddish-brown.
//:
//:  1.- An image can be converted to sepia by taking each pixel, and computing new red, green, and
//:      blue values based on the original values of the three.
//:
//:  2.- There are a number of algorithms for converting an image to sepia, but for this problem,
//:      we’ll ask you to use the following algorithm. For each pixel, the sepia color values should
//:      be calculated based on the original color values per the below.
//:
//>             sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
//>             sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
//>             sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
//:
//:  3.- Of course, the result of each of these formulas may not be an integer, but each value could
//:      be rounded to the nearest integer. It’s also possible that the result of the formula is a
//:      number greater than 255, the maximum value for an 8-bit color value. In that case, the red,
//:      green, and blue values should be capped at 255. As a result, we can guarantee that the
//:      resulting red, green, and blue values will be whole numbers between 0 and 255, inclusive.
//:
//: Write some pseudocode to help you solve this problem and recall the use of nested for loops to
//: visit every pixel.
//:
//>             void sepia(int height, int width, RGBTRIPLE image[height][width])
//>             {
//>                 // Loop over all pixels
//>                 for (int i = 0; i < height; i++)
//>                 {
//>                     for (int j = 0; j < width; j++)
//>                     {
//>                         // Compute sepia values
//>
//>                         // Update pixel with sepia values
//>                     }
//>                 }
//>             }
//:
//: To compute the sepia values, revisit the above bullets. You have a formula to compute the
//: sepia values, but there are still a few catches. In particular, you’ll need to…
//:
//:   1.- Round the result of each computation to the nearest integer
//:
//:   2.- Ensure the resulting value is no larger than 255
//:
//: How might a function that returns the lesser of two integers come in handy while implementing
//: sepia, particularly when you need to make sure a color’s value is no higher than 255? You’re
//: welcome, but not required, to write a helper function of your own to do just that!
//:
//:

//+*************************************************************************************************
//+ Implement reflect
//+*************************************************************************************************
//: Some filters might also move pixels around. Reflecting an image, for example, is a filter where
//: the resulting image is what you would get by placing the original image in front of a mirror.
//:
//:   1.- Any pixels on the left side of the image should end up on the right, and vice versa.
//:
//:   2.- Note that all of the original pixels of the original image will still be present in the
//:       reflected image, it’s just that those pixels may have been rearranged to be in a different
//:       place in the image.
//:
//: In the reflect function, then, you’ll need to swap the values of pixels on opposite sides of a
//: row. Write some pseudocode to help you get started:
//:
//>         void reflect(int height, int width, RGBTRIPLE image[height][width])
//>         {
//>             // Loop over all pixels
//>             for (int i = 0; i < height; i++)
//>             {
//>                 for (int j = 0; j < width; j++)
//>                 {
//>                     // Swap pixels
//>                 }
//>             }
//>         }
//:
//: Recall from lecture how we implemented swapping two values with a temporary variable. No need
//: to use a separate function for swapping unless you would like to!
//:
//: And now’s a good time to think about your nested for loops. The outer for loop iterates over
//: every row, while the inner for loop iterates over every pixel in that row. To successfully
//: reflect a row, though, need you iterate over every pixel in it?
//:
//:


//+*************************************************************************************************
//+ Implement blur
//+*************************************************************************************************
//: There are a number of ways to create the effect of blurring or softening an image. For this
//: problem, we’ll use the “box blur,” which works by taking each pixel and, for each color value,
//: giving it a new value by averaging the color values of neighboring pixels.
//:
//:   1.- Consider the following grid of pixels, where we’ve numbered each pixel.
//:
//:   2.- The new value of each pixel would be the average of the values of all of the pixels that
//:       are within 1 row and column of the original pixel (forming a 3x3 box). For example, each
//:       of the color values for pixel 6 would be obtained by averaging the original color values
//:       of pixels 1, 2, 3, 5, 6, 7, 9, 10, and 11 (note that pixel 6 itself is included in the
//:       average). Likewise, the color values for pixel 11 would be be obtained by averaging the
//:       color values of pixels 6, 7, 8, 10, 11, 12, 14, 15 and 16.
//:
//:   3.- For a pixel along the edge or corner, like pixel 15, we would still look for all pixels
//:       within 1 row and column: in this case, pixels 10, 11, 12, 14, 15, and 16.
//:
//: When implementing the blur function, you might find that blurring one pixel ends up affecting
//: the blur of another pixel. It might be best to create a copy of image by declaring a new,
//: two-dimensional array with code like RGBTRIPLE copy[height][width];. Then copy image into copy,
//: pixel by pixel, with nested for loops, like so:
//:
//: Now, you can read pixels’ colors from copy but write (i.e., change) pixels’ colors in image!
//:
//:


//+*************************************************************************************************
//+ Additional Information
//+*************************************************************************************************
//: 1.- Each function accepts 3 parameters.  Height, width and a pointer to an image structure.
//:
//:   1.1.- image[0] represents the first row of pixels of the image
//:
//:   1.2.- image[Height - 1] is the last row of pixels
//:
//:   1.3.- image[0][0] is the first pixel of the image and image[height - 1][width - 1] is the
//:         last pixel of the image.
//:
//: 2.- Each image pixel has three properties.  They are image.rgbtRed, image.rgbtGreen and
//:     image.rgbtBlue
//:
//: 3.- To get the average and rounded to the nearest integer, then add all the colors, then
//:     divide that number into 3.0 and round the entire result into an integer.
//>               int = round((int + int + int) / 3.0);
//:


#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //: Get the average of all pixels, round it to the nearest integer, and then update all
    //: three color channels to that number
    int new_value = 0;
    for (int r = 0; r < height; r++)
    {
        for (int c= 0; c < width; c++)
        {
            new_value = round((image[r][c].rgbtRed +
                               image[r][c].rgbtGreen +
                               image[r][c].rgbtBlue) / 3.0);

            image[r][c].rgbtRed = new_value;
            image[r][c].rgbtGreen = new_value;
            image[r][c].rgbtBlue = new_value;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed = 0, sepiaGreen = 0, sepiaBlue = 0;
    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < width; c++)
        {
            //> sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
            sepiaRed = round(0.393 * image[r][c].rgbtRed +
                             0.769 * image[r][c].rgbtGreen +
                             0.189 * image[r][c].rgbtBlue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            //> sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
            sepiaGreen = round(0.349 * image[r][c].rgbtRed +
                               0.686 * image[r][c].rgbtGreen +
                               0.168 * image[r][c].rgbtBlue);
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            //> sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
            sepiaBlue = round(0.272 * image[r][c].rgbtRed +
                              0.534 * image[r][c].rgbtGreen +
                              0.131 * image[r][c].rgbtBlue);
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[r][c].rgbtRed = sepiaRed;
            image[r][c].rgbtGreen = sepiaGreen;
            image[r][c].rgbtBlue = sepiaBlue;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //: Get the average of all pixels, round it to the nearest integer, and then update all
    //: three color channels to that number
    RGBTRIPLE temp_pixel = {0};

    /// printf("The width pixels are [%i]\n", width);
    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < (width / 2); c++)
        {
            /// Assume that there are 100 pixels per row.  Then width = 100
            /// The source pixel is [i][j] the target pixel is [i][width - j - 1]
            /// The first pixel
            ///    Left pixel is image[i][j] or image[0][0]
            ///    Right pixel is image[0][width-j-1] or image[0][100-0-1] or image[0][99]
            /// The first pixel
            ///    Left pixel is image[i][j] or image[0][1]
            ///    Right pixel is image[0][width-j-1] or image[0][100-1-1] or image[0][98]


            /// Now load the temp
            temp_pixel = image[r][c];

            /// Now put right into left
            image[r][c] = image[r][width - c - 1];

            /// Now put temp into left
            image[r][width - c - 1] = temp_pixel;

            if (c == (width / 2))
            {
                break;
            }
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Define all the neighbors
    RGBTRIPLE blur[height][width];

    /// Copy array to temp array
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            blur[row][col].rgbtBlue = image[row][col].rgbtBlue;
            blur[row][col].rgbtGreen = image[row][col].rgbtGreen;
            blur[row][col].rgbtRed = image[row][col].rgbtRed;
        }
    }

    int pxl_row;
    int pxl_col;
    int reds;
    int greens;
    int blues;
    int mates_row;
    int mates_col;

    pxl_row = pxl_col = 0;
    float mates = 0.00;

    /// Walk through all pixels, one by one.  When we get a pixel, we will need to
    /// change its reds, greens and blues to be the average of all the "VALID" neighbors
    for (pxl_row = 0; pxl_row < height; pxl_row++)
    {
        for (pxl_col = 0; pxl_col < width; pxl_col++)
        {
            reds = 0, greens = 0, blues = 0;
            mates = 0.00;

            /// Inspect neighbors.  The neighbors are all the pixels that touch the
            /// current [pxl_row][pxl_col] pixel we currently have loaded.  There could
            /// could be up to 9 neighbors although there could be as little as 4, with
            /// the actual pixel included.
            for (mates_row = pxl_row - 1; mates_row < pxl_row + 2; mates_row++)
            {
                for (mates_col = pxl_col - 1; mates_col < pxl_col + 2; mates_col++)
                {
                    /// Is it a valid pixel?.  There is no way in C to safely try to get the
                    /// value of something that does not exist.  Therefore, it is up to me
                    /// to determine which pixels are valid before I try to use them.
                    /// when mates_row < 0, we are not in a valid row since the array starts at
                    /// zero.  But a pixel is invalid if any of its coordinates is beyond the
                    /// bouderies of the pixel array.  If it is invalid, skip it
                    if (mates_row >= 0 && mates_col >= 0 && mates_row <= (height - 1) && mates_col <= (width - 1))
                    {
                        reds += image[mates_row][mates_col].rgbtRed;
                        greens += image[mates_row][mates_col].rgbtGreen;
                        blues += image[mates_row][mates_col].rgbtBlue;
                        mates++;
                    }
                    else
                    {
                        continue;
                    }
                }
            }
            /// Averages now
            blur[pxl_row][pxl_col].rgbtRed = round(reds / mates);
            blur[pxl_row][pxl_col].rgbtGreen = round(greens / mates);
            blur[pxl_row][pxl_col].rgbtBlue = round(blues / mates);
        }
    }



    /// Copy array to temp array
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            image[row][col].rgbtBlue = blur[row][col].rgbtBlue;
            image[row][col].rgbtGreen = blur[row][col].rgbtGreen;
            image[row][col].rgbtRed = blur[row][col].rgbtRed;
        }
    }

    return;
}

/*
// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Define all the neighbors
    RGBTRIPLE blur[height][width];


    /// Let's copy all the pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            blur[i][j].rgbtBlue = image[i][j].rgbtBlue;
            blur[i][j].rgbtGreen = image[i][j].rgbtGreen;
            blur[i][j].rgbtRed = image[i][j].rgbtRed;
        }
    }

    int pxl_row, pxl_col, reds, greens, blues, sample_range_row, sample_range_col;
    int mates_row, mates_col;

    pxl_row = pxl_col = 0;
    float mates = 0.00;

    /// Walk through all pixels, one by one.  When we get a pixel, we will need to
    /// change its reds, greens and blues to be the average of all the "VALID" neighbors
    for (pxl_row = 0; pxl_row < height; pxl_row++)
    {
        for (pxl_col = 0; pxl_col < width; pxl_col++)
        {
            reds = greens = blues = 0;
            mates = 0.00;

            /// Inspect neighbors.  The neighbors are all the pixels that touch the
            /// current [pxl_row][pxl_col] pixel we currently have loaded.  There could
            /// could be up to 9 neighbors although there could be as little as 4, with
            /// the actual pixel included.
            for (sample_range_row = -1; sample_range_row < 2; sample_range_row++)
            {
                for (sample_range_col = 0; sample_range_col < 2; sample_range_col++)
                {
                    /// Get the actual address for the potential neighbor
                    mates_row = pxl_row + sample_range_row;
                    mates_col = pxl_col + sample_range_col;

                    /// Is it a valid pixel?.  There is no way in C to safely try to get the
                    /// value of something that does not exist.  Therefore, it is up to me
                    /// to determine which pixels are valid before I try to use them.
                    /// when mates_row < 0, we are not in a valid row since the array starts at
                    /// zero.  But a pixel is invalid if any of its coordinates is beyond the
                    /// bouderies of the pixel array.  If it is invalid, skip it
                    if (mates_row < 0 || mates_row > (height - 1) || mates_col < 0 || mates_col > (width - 1))
                    {
                        continue;
                    }

                    /// If we are here, we have a valid neighbor pixel.  If it is valid, we can
                    /// add to the running color integers and we can increate the mates count by 1
                    blues += image[mates_row][mates_col].rgbtBlue;
                    greens += image[mates_row][mates_col].rgbtGreen;
                    reds += image[mates_row][mates_col].rgbtRed;

                    mates++;
                }

                /// If we are here, we have investigated and used the values for every VALID pixel
                /// touching the current pixel.  Therefore we can use the average value now, to change
                /// the color channels of the current pixel.
                blur[pxl_row][pxl_col].rgbtBlue = round(blues / mates);
                blur[pxl_row][pxl_col].rgbtGreen = round(greens / mates);
                blur[pxl_row][pxl_col].rgbtRed = round(reds / mates);
            }
        }
    }

    /// Now copy the copy to the orginal
    /// Let's copy all the pixels
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            image[row][col].rgbtBlue = blur[row][col].rgbtBlue;
            image[row][col].rgbtGreen = blur[row][col].rgbtGreen;
            image[row][col].rgbtRed = blur[row][col].rgbtRed;
        }
    }
    return;
}
*/