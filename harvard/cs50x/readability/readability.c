// ***********************************************************************************************
// User Story:
// ***********************************************************************************************
// According to Scholastic, E.B. White’s Charlotte’s Web is between a second- and fourth-grade
// reading level, and Lois Lowry’s The Giver is between an eighth- and twelfth-grade reading
// level. What does it mean, though, for a book to be at a particular reading level?
//
// According to Scholastic, E.B. White’s Charlotte’s Web is between a second- and fourth-grade
// reading level, and Lois Lowry’s The Giver is between an eighth- and twelfth-grade reading
// level. What does it mean, though, for a book to be at a particular reading level?
//
//


// ***********************************************************************************************
// Requirements:
// ***********************************************************************************************
// In a file called readability.c in a folder called readability, you’ll implement a program that
// calculates the approximate grade level needed to comprehend some text. Your program should
// print as output “Grade X” where “X” is the grade level computed, rounded to the nearest
// integer. If the grade level is 16 or higher (equivalent to or greater than a senior
// undergraduate reading level), your program should output “Grade 16+” instead of giving the
// exact index number. If the grade level is less than 1, your program should output “Before
// Grade 1”.
//
//
//


// ***********************************************************************************************
// Background:
// ***********************************************************************************************
// So what sorts of traits are characteristic of higher reading levels? Well, longer words
// probably correlate with higher reading levels. Likewise, longer sentences probably correlate
// with higher reading levels, too.
//
// A number of “readability tests” have been developed over the years that define formulas for
// computing the reading level of a text. One such readability test is the Coleman-Liau index. The
// Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to
// understand some text. The formula is
//
//          index = 0.0588 * L - 0.296 * S - 15.8
//
// where L is the average number of letters per 100 words in the text, and S is the average
// number of sentences per 100 words in the text.
//

// ***********************************************************************************************
// How to test:
// ***********************************************************************************************
// Sample 1:
//     1.- Prompt with "Text: "
//     2.- Enter "One fish. Two fish. Red fish. Blue fish."
//     3.- Print out "Before Grade 1"
//
// Sample 2:
//     1.- Prompt with "Text: "
//     2.- Enter "Congratulations! Today is your day. You're off to Great Places! You're off and
//         away!"
//     3.- Print out "Grade 3"
//
// Sample 3:
//     1.- Prompt with "Text: "
//     2.- Enter "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the
//         summer holidays more than any other time of year. For another, he really wanted to do
//         his homework, but was forced to do it in secret, in the dead of the night. And he also
//         happened to be a wizard."
//     3.- Print out "Grade 5"
//
// Sample 4:
//     1.- Prompt with "Text: "
//     2.- Enter "When he was nearly thirteen, my brother Jem got his arm badly broken at the
//         elbow. When it healed, and Jem's fears of never being able to play football were
//         assuaged, he was seldom self-conscious about his injury. His left arm was somewhat
//         shorter than his right; when he stood or walked, the back of his hand was at right
//         angles to his body, his thumb parallel to his thigh."
//     3.- Print out "Grade 8"
//
// Sample 5:
//     1.- Prompt with "Text: "
//     2.- Enter "A large class of computational problems involve the determination of
//         properties of graphs, digraphs, integers, arrays of integers, finite families of
//         finite sets, boolean formulas and elements of other countable domains."
//     3.- Print out "Grade 16+"
//
// Additional samples:
// 1.- One fish. Two fish. Red fish. Blue fish. --> Before Grade 1
//
// 2.- "Would you like them here or there? I would not like them here or there. I would not like
//      them anywhere." --> Grade 2
//
// 3.- "Congratulations! Today is your day. You're off to Great Places! You're off and away!"
//     --> Grade 3
//
// 4.- "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer
//     holidays more than any other time of year. For another, he really wanted to do his homework
//     , but was forced to do it in secret, in the dead of the night. And he also happened to be
//     a wizard." --> Grade 5



// ***********************************************************************************************
// My pseudo code approach:
// ***********************************************************************************************
// 1.- Prompt the user, with text "Text :"
//
// 2.- Evaluate the text with formula:
//
//          index = 0.0588 * L - 0.296 * S - 15.8
//     L = average number of letters per 100 words
//     S = is the average number of sentences per 100 words
//
// 3.- Assumptions:
//   3.1.- Spaces do not count as letters.
//   3.2.- Need to make sure that you are only counting letters
//   3.3.- A word is any sequence of characters separated by a space
//   3.4.- Assume that the text provided does not start or end with a space
//   3.5.- The end of a sentence is indicated by a period, exclamation point or question mark
//   3.6.- If index is less than 1 assign "Below Grade 1", if 16 or higher then "Grade 16+"
//
//



// ***********************************************************************************************
// Revision 1 specs:
// ***********************************************************************************************
//
//


// ***********************************************************************************************
// Revision 1 pseudo approach:
// ***********************************************************************************************
//
//
//


#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
// #include <stdlib.h>
#include <math.h>

// Prototyping Section
int load_scores(float counters[], string sample);
int get_score(float counters[]);

int main(void)
{
    // Get input from user
    string sample_text = get_string("Text: ");

    float counters[3] = {0};

    // Now pass the array, by reference, and calculate all the scores.
    // counters[0] is the number of letters
    // counters[1] is the number of spaces and then words
    // counters[2] is the number of periods or exclamation marks or question marks
    // and then sentences

    load_scores(counters, sample_text);

    // Computer score
    int score = get_score(counters);

    // Now print out the result
    if (score <= 1)
    {
        // "Below Grade 1", if 16 or higher then "Grade 16+"
        printf("Before Grade 1\n");
    }
    else if (score >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", score);
    }
}

int load_scores(float counters[], string sample)
{
    // printf("Something\n");
    // Let's count all letters first.  If there is at least one letter, then there
    // is also one word and one sentence.
    for (int i = 0, length = strlen(sample); i < length; i++)
    {
        // Count letters
        if (isalpha(sample[i]))
        {
            counters[0] += 1;
        }
        // Count spaces
        if ((int) sample[i] == 32)
        {
            // It is a space so we increase the number of spaces.
            counters[1] += 1;
        }
        // Count sentence markers
        // ASCII value of a period is 46.  Of a exclamation mark it is 33 and question
        // mark is 63
        if (((int) sample[i] == 46) || ((int) sample[i] == 33) || ((int) sample[i] == 63))
        {
            counters[2] += 1;
        }
    }

    // Now calculate the number of words
    counters[1] = counters[1] + 1;

    if (counters[2] == 0)
    {
        counters[2] = 1;
    }

    return 1;
}

int get_score(float counters[])
{
    //index = 0.0588 * L - 0.296 * S - 15.8
    // L = (Letters ÷ Words) × 100
    // S = (Sentences ÷ Words) × 100
    float index = 0.0;
    float L = 0.0;
    float S = 0.0;

    // printf("The number of letters is [%f]\n", counters[0]);
    // printf("The number of words is [%f]\n", counters[1]);
    // printf("The number of sentences is [%f]\n", counters[2]);

    L = (counters[0] / counters[1]) * 100.0;
    // printf("The value for L is [%f]\n", L);

    S = (counters[2] / counters[1]) * 100.0;
    // printf("The value for S is [%f]\n", S);

    index = 0.0588 * L - 0.296 * S - 15.8;

    // printf("The index is [%lf]\n", index);
    int rounded = 0;
    rounded = round(index);
    // printf("The rounded index is [%i]\n", rounded);

    return rounded;
}
