//.*************************************************************************************************
//. User Story:
//.*************************************************************************************************
/// You already know about plurality elections, which follow a very simple algorithm for
/// determining the winner of an election: every voter gets one vote, and the candidate with the
/// most votes wins.
///
/// But the plurality vote does have some disadvantages. What happens, for instance, in an election
/// with three candidates, and the ballots below are cast?
///
/// A plurality vote would here declare a tie between Alice and Bob, since each has two votes. But
/// is that the right outcome?
///
/// There’s another kind of voting system known as a ranked-choice voting system. In a ranked-choice
/// system, voters can vote for more than one candidate. Instead of just voting for their top
/// choice, they can rank the candidates in order of preference. The resulting ballots might
/// therefore look like the below.
///
//>      Ballot
//>      1.- Alice
//>      2.- Bob
//>      3.- Charlie
///
/// Here, each voter, in addition to specifying their first preference candidate, has also
/// indicated their second and third choices. And now, what was previously a tied election could
/// now have a winner. The race was originally tied between Alice and Bob, so Charlie was out of
/// the running. But the voter who chose Charlie preferred Alice over Bob, so Alice could here be
/// declared the winner.
///
/// Ranked choice voting can also solve yet another potential drawback of plurality voting. Take a
/// look at the following ballots.
///
///          Sample on the web page
///
/// Who should win this election? In a plurality vote where each voter chooses their first
/// preference only, Charlie wins this election with four votes compared to only three for Bob and
/// two for Alice. But a majority of the voters (5 out of the 9) would be happier with either Alice
/// or Bob instead of Charlie. By considering ranked preferences, a voting system may be able to
/// choose a winner that better reflects the preferences of the voters.
///
/// One such ranked choice voting system is the instant runoff system. In an instant runoff
/// election, voters can rank as many candidates as they wish. If any candidate has a majority
/// (more than 50%) of the first preference votes, that candidate is declared the winner of the
/// election.
///
/// If no candidate has more than 50% of the vote, then an “instant runoff” occurs. The candidate
/// who received the fewest number of votes is eliminated from the election, and anyone who
/// originally chose that candidate as their first preference now has their second preference
/// considered. Why do it this way? Effectively, this simulates what would have happened if the
/// least popular candidate had not been in the election to begin with.
///
/// The process repeats: if no candidate has a majority of the votes, the last place candidate
/// is eliminated, and anyone who voted for them will instead vote for their next preference
/// (who hasn’t themselves already been eliminated). Once a candidate has a majority, that
/// candidate is declared the winner.
///
/// Sounds a bit more complicated than a plurality vote, doesn’t it? But it arguably has the
/// benefit of being an election system where the winner of the election more accurately
/// represents the preferences of the voters. In a file called runoff.c in a folder called
/// runoff, create a program to simulate a runoff election.
///
///

//.*************************************************************************************************
//. Understand the code in runoff.c
//.*************************************************************************************************
/// Whenever you’ll extend the functionality of existing code, it’s best to be sure you first
/// understand it in its present state.
///
/// Look at the top of runoff.c first. Two constants are defined: MAX_CANDIDATES for the maximum
/// number of candidates in the election, and MAX_VOTERS for the maximum number of voters in the
/// election
///
//<                  Max voters and candidates
//<                  #define MAX_VOTERS 100
//<                  #define MAX_CANDIDATES 9
///
/// Notice that MAX_CANDIDATES is used to size an array, candidates.
///
//<                 // Array of candidates
//<                 candidate candidates[MAX_CANDIDATES];
///
/// candidates is an array of candidates. In runoff.c a candidate is a struct. Every candidate has a
/// string field for their name, an int representing the number of votes they currently have, and a
/// bool value called eliminated that indicates whether the candidate has been eliminated from the
/// election. The array candidates will keep track of all of the candidates in the election.
///
//<                 // Candidates have name, vote count, eliminated status
//<                 typedef struct
//<                 {
//<                     string name;
//<                     int votes;
//<                     bool eliminated;
//<                 }
//<                 candidate;
///
/// Now you can better understand preferences, the two-dimensional array. The array preferences[i]
/// will represent all of the preferences for voter number i. The integer, preferences[i][j], will
/// store the index of the candidate, from the candidates array, who is the jth preference for
/// voter i.
///
//<                 // preferences[i][j] is jth preference for voter i
//<                 int preferences[MAX_VOTERS][MAX_CANDIDATES];
///
/// The program also has two global variables: voter_count and candidate_count.
///
//<                 // Numbers of voters and candidates
//<                 int voter_count;
//<                 int candidate_count;
///
/// Now onto main. Notice that after determining the number of candidates and the number of voters,
/// the main voting loop begins, giving every voter a chance to vote. As the voter enters their
/// preferences, the vote function is called to keep track of all of the preferences. If at any
/// point, the ballot is deemed to be invalid, the program exits.
///
/// Once all of the votes are in, another loop begins: this one’s going to keep looping through the
/// runoff process of checking for a winner and eliminating the last place candidate until there is
/// a winner.
///
/// The first call here is to a function called tabulate, which should look at all of the voters’
/// preferences and compute the current vote totals, by looking at each voter’s top choice candidate
/// who hasn’t yet been eliminated. Next, the print_winner function should print out the winner if
/// there is one; if there is, the program is over. But otherwise, the program needs to determine
/// the fewest number of votes anyone still in the election received (via a call to find_min). If
/// it turns out that everyone in the election is tied with the same number of votes (as determined
/// by the is_tie function), the election is declared a tie; otherwise, the last-place candidate
/// (or candidates) is eliminated from the election via a call to the eliminate function.
///
/// If you look a bit further down in the file, you’ll see that the rest of the functions—vote,
/// tabulate, print_winner, find_min, is_tie, and eliminate—are all left to up to you to complete!
/// You should only modify these functions in runoff.c, though you may #include additional header
/// files atop runoff.c if you’d like
///

//.*************************************************************************************************
//. Complete the vote function
//.*************************************************************************************************
/// 1.- Complete the vote function.
///
///   1.1.- The function takes three arguments: voter, rank, and name.
///
///   1.2.- If name is a match for the name of a valid candidate, then you should update the global
///         preferences array to indicate that the voter voter has that candidate as their rank
///         preference. Keep in mind 0 is the first preference, 1 is the second preference, etc. You
///         may assume that no two candidates will have the same name.
///
///   1.3.- If the preference is successfully recorded, the function should return true. The
///         function should return false otherwise. Consider, for instance, when name is not the
///         name of one of the candidates.
///
/// 2.- As you write your code, consider these hints:
///
///   2.1.- Recall that candidate_count stores the number of candidates in the election.
///
///   2.2.- Recall that you can use strcmp to compare two strings.
///
///   2.3.- Recall that preferences[i][j] stores the index of the candidate who is the jth ranked
///         preference for the ith voter.
///

//.*************************************************************************************************
//. Complete the tabulate function
//.*************************************************************************************************
/// 1.- Complete the tabulate function.
///
///   1.1.- The function should update the number of votes each candidate has at this stage in the
///         runoff.
///
///   1.2.- Recall that at each stage in the runoff, every voter effectively votes for their
///         top-preferred candidate who has not already been eliminated.
///
/// 2.- As you write your code, consider these hints:
///
///   2.1.- Recall that voter_count stores the number of voters in the election and that, for each
///         voter in our election, we want to count one ballot.
///
///   2.2.- Recall that for a voter i, their top choice candidate is represented by preferences[i][0],
///         their second choice candidate by preferences[i][1], etc.
///
///   2.3.- Recall that the candidate struct has a field called eliminated, which will be true if the
///         candidate has been eliminated from the election.
///
///   2.4.- Recall that the candidate struct has a field called votes, which you’ll likely want to
///         update for each voter’s preferred candidate.
///
///   2.5.- Recall that once you’ve cast a vote for a voter’s first non-eliminated candidate, you’ll
///         want to stop there, not continue down their ballot. You can break out of a loop early
///         using break inside of a conditional.
///
///
///

//.*************************************************************************************************
//. Complete the print_winner function
//.*************************************************************************************************
/// 1.- Complete the print_winner function.
///
///   1.1.- If any candidate has more than half of the vote, their name should be printed and the
///         function should return true.
///
///   1.2.- If nobody has won the election yet, the function should return false.
///
/// 2.- As you write your code, consider this hint:
///
///   2.1.- Recall that voter_count stores the number of voters in the election. Given that, how
///         would you express the number of votes needed to win the election?
///
///

//.*************************************************************************************************
//. Complete the find_min function.
//.*************************************************************************************************
/// 1.- Complete the find_min function.
///
///   1.1.- The function should return the minimum vote total for any candidate who is still in the
///         election.
///
/// 2.- As you write your code, consider this hint:
///
///   2.1.- You’ll likely want to loop through the candidates to find the one who is both still in
///         the election and has the fewest number of votes. What information should you keep track
///         of as you loop through the candidates?
///
///

//.*************************************************************************************************
//. Complete the is_tie function.
//.*************************************************************************************************
/// 1.- Complete the is_tie function.
///
///   1.1.- The function takes an argument min, which will be the minimum number of votes that
///         anyone in the election currently has.
///
///   1.2.- The function should return true if every candidate remaining in the election has the same
///         number of votes, and should return false otherwise.
///
/// 2.- As you write your code, consider this hint:
///
///   2.1.- Recall that a tie happens if every candidate still in the election has the same number of
///         votes. Note, too, that the is_tie function takes an argument min, which is the smallest
///         number of votes any candidate currently has. How might you use min to determine if the
///         election is a tie (or, conversely, not a tie)?
///
///

//.*************************************************************************************************
//. Complete the eliminate function.
//.*************************************************************************************************
/// 1.- Complete the eliminate function.
///
///   1.1.- The function takes an argument min, which will be the minimum number of votes that
///         anyone in the election currently has.
///
///   1.2.- The function should eliminate the candidate (or candidates) who have min number of
///         votes.
///
///


//.*************************************************************************************************
//. My pseudo code
//.*************************************************************************************************
/// 1.- If any candidate gets more than 50% of the vote, that candidate wins
///
/// 2.- If no candidate has more than 50% of the vote, we eliminate the lowest candidate and run the
///     election again.
///
///   2.1.- When the lowest candidate gets eliminated, take that candidate's ballots and sum up the
///         second and third place placements add assign those values to the remaining candidates.
///
/// 3.- System will need to track what the voters have done and I am asked to track that in a two
///     dimensional array.  Assume example voter[i][j] and that there are 3 candidates.
///
///   3.1.- Assume that Alice is the first candidate and she is stored in the candidates array pos
///         0, Bob is in pos 1 and Charlie is in pos 2.
///
///   3.2.- The first dimension[i] represents the voter itself.  "i" represents the number of voters
///
///   3.3.- The second dimension [j] represents the voters preferences.  "j" will equal the amount
///         of candidates.
///
///   3.4.- Assume a ballot where the slot 1 goes to Charlie, second slot goes to Alice and the
///         third slot goes to Bob
///
///   3.5.- The voter's array would have:
///
///              voter[0][0] = 2            // Since Charlie is in pos 2 of the candidate's array
///              voter[0][1] = 0            // Since Alice is in pos 0 of the candidate's array
///              voter[0][2] = 1            // Since Bob is in pos 1 of the candidate's array
///
///

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;
char testing = 'N';

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    //testing = get_char("Are we testing: ");

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }
        if (testing == 'Y')
        {
            printf("Vote recorded for voter [%i]\n", i);
            printf("---- Top position is        [%i]\n", preferences[i][0]);
            printf("---- Second position is     [%i]\n", preferences[i][1]);
            printf("---- Third position is      [%i]\n", preferences[i][2]);
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        if (testing == 'Y')
        {
            printf("Candidate [%s]\n", candidates[0].name);
            printf("---- Has a total of [%i]\n", candidates[0].votes);
            if (candidates[0].eliminated)
            {
                printf("---- Eliminated status is true\n");
            }
            else
            {
                printf("---- Eliminated status is false\n");
            }

            printf("Candidate [%s]\n", candidates[1].name);
            printf("---- Has a total of [%i]\n", candidates[1].votes);
            if (candidates[1].eliminated)
            {
                printf("---- Eliminated status is true\n");
            }
            else
            {
                printf("---- Eliminated status is false\n");
            }

            printf("Candidate [%s]\n", candidates[2].name);
            printf("---- Has a total of [%i]\n", candidates[2].votes);
            if (candidates[2].eliminated)
            {
                printf("---- Eliminated status is true\n");
            }
            else
            {
                printf("---- Eliminated status is false\n");
            }
        }

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();

        if (testing == 'Y')
        {
            printf("The result from find_min is [%i]\n", min);
        }

        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    /// voter
    ///    Is the number of the current voter
    /// rank
    ///    Is the rank position the voter is voting for.  Position zero is their top
    ///    preference.
    /// name
    ///    Is the name of the candidate
    /// Actions
    ///    1.- Look for a candidate called name.  The position in which you find the
    ///        candidate, represents what value you will store in the voter's
    ///        preference.
    ///    2.- Update the two dimensional array to store that voter's preference
    ///    3.- Return true if you are able to store the value or false if not.

    /// What is the size of the candidate array? candidate_count.
    /// candidate_count is the number of arguments minus one.  If they put in 3
    /// candidates, then this number will be (4 - 1)
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    /// Tabulate all the votes for each candidate
    /// 1.- Loop through the preference array for each voter.  That is dimension 1
    /// 2.- In each pass look for the candidate selected in the lowest position
    ///    2.1.- If that candidate has been eliminated, you need to look at the
    ///          next position
    ///    2.2.- The first candidate that has not been eliminated gets the vote.
    int voted_for;
    // candidates[1].eliminated = true;
    for (int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            voted_for = preferences[i][j];
            if (!candidates[voted_for].eliminated)
            {
                candidates[voted_for].votes += 1;
                j = candidate_count;
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    int required = 0, how_many = 0, who = -1;
    required = (voter_count / 2) + 1;

    if (testing == 'Y')
    {
        printf("The winner needs a total of [%i] votes\n", required);
    }

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes >= required)
        {
            who = i;
            how_many += 1;
        }
    }

    if (how_many == 1)
    {
        printf("%s\n", candidates[who].name);
        return true;
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    /// Minimum number of votes of anyone still in the election
    /// Only non eliminated candidates
    int min_votes = MAX_VOTERS;
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated)
        {
            if (candidates[i].votes < min_votes)
            {
                min_votes = candidates[i].votes;
            }
        }
    }
    if (min_votes <= MAX_VOTERS - 1)
    {
        return min_votes;
    }
    return 0;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    /// Returns true if all remaining candidates has the min score.
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated)
        {
            if (!(candidates[i].votes == min))
            {
                return false;
            }
        }
    }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    /// Eliminate all the candidates whose votes equal the min amount passed
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }
    return;
}
