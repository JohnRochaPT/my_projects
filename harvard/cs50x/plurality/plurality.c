// ***********************************************************************************************
// User Story:
// ***********************************************************************************************
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//

// ***********************************************************************************************
// Requirements:
// ***********************************************************************************************
// Next, complete the vote function
//
// 1.- Consider that vote’s signature, bool vote(string name), shows it takes a single argument,
//     a string called name, representing the name of the candidate who was voted for.
//
// 2.- vote should return a bool, where true indicates a vote was successfully cast and false
//     indicates it was not.
//
// One way to approach this problem is to do the following:
// 1.- Iterate over each candidate
//
//   1.1.- Check if candidate’s name matches the input, name
//
//       1.1.1.- If yes, increment that candidate’s votes and return true
//
//       1.1.2.- If no, continue checking
//
//   1.2.- If no matches after checking each candidate, return false
//
// Let’s write some pseudocode to remind you to do just that:
//              // Update vote totals given a new vote
//              bool vote(string name)
//              {
//                  // Iterate over each candidate
//                      // Check if candidate's name matches given name
//                          // If yes, increment candidate's votes and return true
//
//                // If no match, return false
//              }
//
// Finally, complete the print_winner function
//    1.- The function should print out the name of the candidate who received the most votes
//        in the election, and then print a newline.
//
//    2.- The election could end in a tie if multiple candidates each have the maximum number
//        of votes. In that case, you should output the names of each of the winning
//        candidates, each
//     on a separate line.
//
// You might think a sorting algorithm would best solve this problem: imagine sorting candidates
// by their vote totals and printing the top candidate (or candidates). Recall, though, that
// sorting can be expensive: even Merge Sort, one of the fastest sorting algorithms, runs
// in O(N log (N))
//
// Consider that you need only two pieces of information to solve this problem:
//    1.- The maximum number of votes
//
//    2.- The candidate (or candidates) with that number of votes
//
//                  // Print the winner (or winners) of the election
//                  void print_winner(void)
//                  {
//                      // Find the maximum number of votes
//
//                      // Print the candidate (or candidates) with maximum votes
//
//                  }
//
//



// ***********************************************************************************************
// How to test:
// ***********************************************************************************************
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//


// ***********************************************************************************************
// My pseudo code approach:
// ***********************************************************************************************
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//



#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    // name contains the actual name of the person who the vote is supposed to be
    // going to
    for (int i = 0; i < MAX; i++)
    {
        // printf("Loop [%i] has name [%s]\n", i, candidates[i].name);
        if (candidates[i].name != NULL)
        {
            if (strcmp(candidates[i].name, name) == 0)
            {
                //printf("Vote added to [%s]\n", candidates[i].name);
                candidates[i].votes += 1;
                return true;
            }
        }
        else
        {
            return false;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // Similar to above
    // I think I need to get the highest score first.
    int highest_score = 0;
    int loop_counter;
    for (loop_counter = 0; loop_counter < MAX; loop_counter++)
    {
        if (candidates[loop_counter].name != NULL)
        {
            if (highest_score < candidates[loop_counter].votes)
            {
                highest_score = candidates[loop_counter].votes;
            }
        }
    }

    if (highest_score > 0)
    {
        for (int i = 0; i <= loop_counter; i++)
        {
            if (candidates[i].votes == highest_score)
            {
                printf("%s\n", candidates[i].name);
            }
        }
    }

    return;
}
