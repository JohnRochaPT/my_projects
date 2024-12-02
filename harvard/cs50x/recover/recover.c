//+*************************************************************************************************
//+ User Story:
//+*************************************************************************************************
//: In anticipation of this problem, we spent the past several days taking photos around campus, all
//: of which were saved on a digital camera as JPEGs on a memory card. Unfortunately, we somehow
//: deleted them all! Thankfully, in the computer world, “deleted” tends not to mean “deleted” so
//: much as “forgotten.” Even though the camera insists that the card is now blank, we’re pretty
//: sure that’s not quite true. Indeed, we’re hoping (er, expecting!) you can write a program that
//: recovers the photos for us!
//:
//: In a file called recover.c in a folder called recover, write a program to recover JPEGs from a
//: memory card.
//:
//:


//+*************************************************************************************************
//+ Background:
//+*************************************************************************************************
//: Even though JPEGs are more complicated than BMPs, JPEGs have “signatures,” patterns of bytes
//: that can distinguish them from other file formats. Specifically, the first three bytes of JPEGs
//: are:
//:
//>             0xff 0xd8 0xff
//:
//: from first byte to third byte, left to right. The fourth byte, meanwhile, is either 0xe0, 0xe1,
//: 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee, or 0xef. Put
//: another way, the fourth byte’s first four bits are 1110.
//:
//: Odds are, if you find this pattern of four bytes on media known to store photos (e.g., my memory
//: card), they demarcate the start of a JPEG. To be fair, you might encounter these patterns on
//: some disk purely by chance, so data recovery isn’t an exact science.
//:
//: Fortunately, digital cameras tend to store photographs contiguously on memory cards, whereby
//: each photo is stored immediately after the previously taken photo. Accordingly, the start of a
//: JPEG usually demark the end of another. However, digital cameras often initialize cards with a
//: FAT file system whose “block size” is 512 bytes (B). The implication is that these cameras only
//: write to those cards in units of 512 B. A photo that’s 1 MB (i.e., 1,048,576 B) thus takes up
//: 1048576 ÷ 512 = 2048 “blocks” on a memory card. But so does a photo that’s, say, one byte
//: smaller (i.e., 1,048,575 B)! The wasted space on disk is called “slack space.” Forensic
//: investigators often look at slack space for remnants of suspicious data.
//:
//: The implication of all these details is that you, the investigator, can probably write a
//: program that iterates over a copy of my memory card, looking for JPEGs’ signatures. Each time
//: you find a signature, you can open a new file for writing and start filling that file with
//: bytes from my memory card, closing that file only once you encounter another signature.
//: Moreover, rather than read my memory card’s bytes one at a time, you can read 512 of them at
//: a time into a buffer for efficiency’s sake. Thanks to FAT, you can trust that JPEGs’
//: signatures will be “block-aligned.” That is, you need only look for those signatures in a
//: block’s first four bytes.
//:
//: Realize, of course, that JPEGs can span contiguous blocks. Otherwise, no JPEG could be larger
//: than 512 B. But the last byte of a JPEG might not fall at the very end of a block. Recall the
//: possibility of slack space. But not to worry. Because this memory card was brand-new when I
//: started snapping photos, odds are it’d been “zeroed” (i.e., filled with 0s) by the
//: manufacturer, in which case any slack space will be filled with 0s. It’s okay if those
//: trailing 0s end up in the JPEGs you recover; they should still be viewable.
//:
//: Now, I only have one memory card, but there are a lot of you! And so I’ve gone ahead and
//: created a “forensic image” of the card, storing its contents, byte after byte, in a file
//: called card.raw. So that you don’t waste time iterating over millions of 0s unnecessarily,
//: I’ve only imaged the first few megabytes of the memory card. But you should ultimately find
//: that the image contains 50 JPEGs.
//:
//:

//+*************************************************************************************************
//+ Specification:
//+*************************************************************************************************
//: Implement a program called recover that recovers JPEGs from a forensic image.
//:
//:  1.- Implement your program in a file called recover.c in a directory called recover.
//:
//:  2.- Your program should accept exactly one command-line argument, the name of a forensic image
//:      from which to recover JPEGs.
//:
//:  3.- If your program is not executed with exactly one command-line argument, it should remind
//:      the user of correct usage, and main should return 1.
//:
//:  4.- If the forensic image cannot be opened for reading, your program should inform the user as
//:      much, and main should return 1.
//:
//:  5.- The files you generate should each be named ###.jpg, where ### is a three-digit decimal
//:      number, starting with 000 for the first image and counting up.
//:
//:  6.- Your program, if it uses malloc, must not leak any memory.
//:
//:


//+*************************************************************************************************
//+ Requirements:
//+*************************************************************************************************
//: If unsure how to solve the larger problem, break it down into smaller problems that you can
//: probably solve first. For instance, this problem is really only a handful of problems:
//:
//: 1.- Accept a single command-line argument: the name of a memory card
//:
//: 2.- Open the memory card
//:
//: 3.- While there’s still data left to read in the memory card
//:
//:   3.1.- Create JPEGs from the data
//:
//: Let’s write some pseudocode as comments to remind you to do just that:
//:
//>             #include <stdio.h>
//>             #include <stdlib.h>
//>
//>             int main(int argc, char *argv[])
//>             {
//>                 // Accept a single command-line argument
//>
//>                 // Open the memory card
//>
//>                 // While there's still data left to read from the memory card
//>
//>                     // Create JPEGs from the data
//>             }
//:
//: 4.- Keep your working directory clean
//:
//:   4.1.- Odds are the JPEGs that the first draft of your code spits out won’t be correct. (If you
//:         open them up and don’t see anything, they’re probably not correct!) Execute the command
//:         below to delete all JPEGs in your current working directory.
//:
//>              rm *.jpg
//>
//>                 or
//>
//>             rm -f *.jpg
//:
//:


//+*************************************************************************************************
//+ Additional Requirements:
//+*************************************************************************************************
//: TODO
//: 1.- Open memory card
//:
//: 2.- Look for the beginning of a JPEG file
//:
//: 3.- Open a new JPEG file
//:
//: 4.- Write 512 bytes until a new JPEG file is found.  At this point, close the current file,
//:     open a new file and start all over again.
//:
//: Process:
//: 1.- Open memory card
//:
//:    FILE *f = fopen(filename, "r");
//:
//: 2.- Inspect the file.
//:
//:   2.1.- The start of a JPEG file always starts with 0xff, then 0xd8, then 0xff and the fourth
//:         bite is 0xe"0" through "f".  If you find this pattern, it is the beginning of a jpeg file
//:
//: 3.- Once you have a new header, open a new file and save the header to the new file.
//:
//: 4.- Each time you read, you will get 512 bytes.
//:
//:   4.1.- Use fread(data, size, number, inptr);
//:
//:     "data" is a pointer where you are going to store the data you just read
//:
//:     "size" is the size of elements you are going to read
//:
//:     "number" is the number of elements you are going to read
//:
//:     "inptr" FILE * to read from
//:
//:   4.2.- Check the first 3 bytes for a header.  Then check the fourth using bitwise "and" by
//:         looking at the first four bits as below:
//:
//:         (buffer[3] & 0xf0) == 0xe0  -->  What is happening here is that we use the & bitwise
//:                                          arithmetic and apply it to the value in buffer[3].  If
//:                                          the bite results in 0xe0; it is valid sinc all 0xe0
//:                                          through 0xef when "anded" with 0xf0, result in 0xe0
//:
//:   4.3.- If you find the pattern above, you have a new JPEG file.  At this point, create a new
//:         file that you will write to.
//:
//:      4.3.1.- File name ###.jpg and keep track of how many files you found so far.  Start with
//:              "000.jpg"
//:      4.3.2.- You can use function
//>                   sprintf(filename, "%03i.jpg", 2);
//:
//:      4.3.3.- Open a new file with the file name above with
//>                   FILE *img = fopen(filename, "w");
//:
//:      4.3.3.- Write to the file with
//:
//>                   fwrite(data, size, number, outptr);
//:
//:             "data" pointer to bytes that you will be written to file
//:
//:             "size" is the size of elements you are going to write
//:
//:             "number" is the number of elements you are going to write
//:
//:             "inptr" FILE * to write to
//:
//:   4.4.- fread returns the number of items of size "size" that were read
//:

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
// #include <stdbool.h>
#include <cs50.h>

/// Prototypes



int main(int argc, char *argv[])
{
    /// Check passed arguments
    /// Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    /// Open the memory card
    FILE *src = fopen(argv[1], "r");
    FILE *img;
    if (src == NULL)
    {
        printf("File [%s] does not exist\n",argv[1]);
        return 2;
    }


    /// Working variables
    uint8_t buffer[512];
    int file_count = 0, bytes_read = 0;
    char file_name[8] = "000.jpg";
    bool reading = false, writing = false;

    /// Initial read.  Must read at least 512 bytes the first time around
    bytes_read = fread(buffer, 1, 512, src);
    if (!(bytes_read == 512))
    {
        /// printf("Unable to complete the first read\n");
        fclose(src);
        return 3;
    }


    /// If we are here, we are reading
    reading = true;

    /// Now we can loop
    while (reading)
    {
        /// Check if we are at the end
        if (bytes_read < 512)
        {
            /// We are at the end and need to close and exit
            reading = false;
            fclose(img);
            break;
        }
        /// If it is the start of a new file, open a new file to write to
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            /// If there are no jpg files opened, open a new one.  If there is one open, close
            /// it and open a new one with the same pointer.
            if (file_count > 0)
            {
                fclose(img);
            }

            /// Open a new file
            sprintf(file_name, "%03i.jpg", file_count);
            /// printf("The file name we are writing is [%s]\n", file_name);
            img = fopen(file_name, "w");
            file_count++;
            writing = true;
        }

        /// If we have a file open for read, we can write to it
        if (writing)
        {
            fwrite(buffer, 512, 1, img);
            /// printf("wrote to file [%s]\n", file_name);
        }

        /// Here we should write to file
        bytes_read = fread(buffer, 1, 512, src);
        /// printf("Read [%i] bytes\n", bytes_read);
    }


    fclose(src);
    return 0;
}
