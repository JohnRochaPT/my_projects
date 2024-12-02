//+*************************************************************************************************
//+ Problem to Solve:
//+*************************************************************************************************
//: A person’s blood type is determined by two alleles (i.e., different forms of a gene). The three
//: possible alleles are A, B, and O, of which each person has two (possibly the same, possibly
//: different). Each of a child’s parents randomly passes one of their two blood type alleles to
//: their child. The possible blood type combinations, then, are: OO, OA, OB, AO, AA, AB, BO, BA,
//: and BB.
//:
//: For example, if one parent has blood type AO and the other parent has blood type BB, then the
//: child’s possible blood types would be AB and OB, depending on which allele is received from each
//: parent. Similarly, if one parent has blood type AO and the other OB, then the child’s possible
//: blood types would be AO, OB, AB, and OO.
//:
//: In a file called inheritance.c in a folder called inheritance, simulate the inheritance of blood
//: types for each member of a family.
//:
//:


//+*************************************************************************************************
//+ Implementation Details:
//+*************************************************************************************************
//: Complete the implementation of inheritance.c, such that it creates a family of a specified
//: generation size and assigns blood type alleles to each family member. The oldest generation will
//: have alleles assigned randomly to them.
//:
//: 1.- The create_family function takes an integer (generations) as input and should allocate (as
//:     via malloc) one person for each member of the family of that number of generations,
//:     returning a pointer to the person in the youngest generation.
//:
//:   1.1.- For example, create_family(3) should return a pointer to a person with two parents,
//:         where each parent also has two parents.
//:
//:   1.2.- Each person should have alleles assigned to them. The oldest generation should have
//:         alleles randomly chosen (as by calling the random_allele function), and younger
//:         generations should inherit one allele (chosen at random) from each parent.
//:
//:   1.4.- Each person should have parents assigned to them. The oldest generation should have both
//:         parents set to NULL, and younger generations should have parents be an array of two
//:         pointers, each pointing to a different parent.
//:
//:

//+*************************************************************************************************
//+ Hints: Understand the code in inheritance.c
//+*************************************************************************************************
//: Take a look at the distribution code in inheritance.c.
//:
//: Notice the definition of a type called person. Each person has an array of two parents, each of
//: which is a pointer to another person struct. Each person also has an array of two alleles, each
//: of which is a char (either 'A', 'B', or 'O').
//:
//>         // Each person has two parents and two alleles
//>         typedef struct person
//>         {
//>             struct person *parents[2];
//>             char alleles[2];
//>         }
//>         person;
//:
//: Now, take a look at the main function. The function begins by “seeding” (i.e., providing some
//: initial input to) a random number generator, which we’ll use later to generate random alleles.
//:
//>         // Seed random number generator
//>         srand(time(0));
//:
//: The main function then calls the create_family function to simulate the creation of person
//: structs for a family of 3 generations (i.e. a person, their parents, and their grandparents).
//:
//>         // Create a new family with three generations
//>         person *p = create_family(GENERATIONS);
//:
//: We then call print_family to print out each of those family members and their blood types.
//:
//>         // Print family tree of blood types
//>         print_family(p, 0);
//:
//: Finally, the function calls free_family to free any memory that was previously allocated with
//: malloc.
//:
//>         // Free memory
//>         free_family(p);
//:
//: The create_family and free_family functions are left to you to write!
//:



//+*************************************************************************************************
//+ Hints: Complete the create_family function
//+*************************************************************************************************
//: The create_family function should return a pointer to a person who has inherited their blood
//: type from the number of generations given as input.
//:
//:   1.- Notice first that this problem poses a good opportunity for recursion.
//:
//:     1.1.- To determine the present person’s blood type, you need to first determine their
//:           parents’ blood types.
//:
//:     1.2.- To determine those parents’ blood types, you must first determine their parents’ blood
//:           types. And so on until you reach the last generation you wish to simulate.
//:
//: To solve this problem, you’ll find several TODOs in the distribution code.
//:
//: First, you should allocate memory for a new person. Recall that you can use malloc to allocate
//: memory, and sizeof(person) to get the number of bytes to allocate.
//:
//>             // Allocate memory for new person
//>             ...
//:
//: Next, you should check if there are still generations left to create: that is, whether
//: generations > 1.
//:
//: If generations > 1, then there are more generations that still need to be allocated. We’ve
//: already created two new parents, parent0 and parent1, by recursively calling create_family. Your
//: create_family function should then set the parent pointers of the new person you created.
//: Finally, assign both alleles for the new person by randomly choosing one allele from each parent.
//:
//:   2.- Remember, to access a variable via a pointer, you can use arrow notation. For example, if
//:       p is a pointer to a person, then a pointer to this person’s first parent can be accessed
//:       by p->parents[0].
//:
//:   3.- You might find the rand() function useful for randomly assigning alleles. This function
//:       returns an integer between 0 and RAND_MAX, or 32767. In particular, to generate a
//:       pseudorandom number that is either 0 or 1, you can use the expression rand() % 2.
//:
//>             // Create two new parents for current person by recursively calling create_family
//>             ...
//>             ...
//>
//>             // Set parent pointers for current person
//>             ...
//>             ...
//>
//>             // Randomly assign current person's alleles based on the alleles of their parents
//>             ...
//>             ...
//>
//:
//: Let’s say there are no more generations left to simulate. That is, generations == 1. If so,
//: there will be no parent data for this person. Both parents of your new person should be set to
//: NULL, and each allele should be generated randomly.
//:
//>             // Set parent pointers to NULL
//>             ...
//>             ...
//>
//>             // Randomly assign alleles
//>             ...
//>             ...
//:
//: Finally, your function should return a pointer for the person that was allocated.
//:
//>             // Return newly created person
//>             ...
//>             ...
//:
//:


//+*************************************************************************************************
//+ Hints: Complete the free_family function
//+*************************************************************************************************
//: The free_family function should accept as input a pointer to a person, free memory for that
//: person, and then recursively free memory for all of their ancestors.
//:
//:   1.- Since this is a recursive function, you should first handle the base case. If the input to
//:       the function is NULL, then there’s nothing to free, so your function can return
//:       immediately.
//:
//:   2.- Otherwise, you should recursively free both of the person’s parents before freeing the
//:       child.
//:
//: The below is quite the hint, but here’s how to do just that!
//:
//:


//+*************************************************************************************************
//+ How to Test
//+*************************************************************************************************
//: Upon running ./inheritance, your program should adhere to the rules described in the
//: background. The child should have two alleles, one from each parent. The parents should each
//: have two alleles, one from each of their parents.
//:
//: For example, in the example below, the child in Generation 0 received an O allele from both
//: Generation 1 parents. The first parent received an A from the first grandparent and a O from the
//: second grandparent. Similarly, the second parent received an O and a B from their grandparents.
//:
//>         $ ./inheritance
//>         Child (Generation 0): blood type OO
//>             Parent (Generation 1): blood type AO
//>                 Grandparent (Generation 2): blood type OA
//>                 Grandparent (Generation 2): blood type BO
//>             Parent (Generation 1): blood type OB
//>                 Grandparent (Generation 2): blood type AO
//>                 Grandparent (Generation 2): blood type BO
//:
//:


//+*************************************************************************************************
//+  Additional information from Walkthrough videos
//+*************************************************************************************************
//: 1.- Each family will have three generations only
//:
//: 2.- Complete the code to create a family with 3 generations
//:
//:   2.1.- Allocate memory to create a new person.
//:
//:   2.2.- You will need to recursively call the create person function to build the parents and
//:         grandparents.
//:
//:   2.3.- Once the parents are created you will need to start with the grandparents and randomly
//:         select their blood type and then use those values to determine the children blood type
//:
//:   2.4.- If you are at generation 1, then you will need to set the parents to NULL and randomly
//:         assign their alleles
//:
//: 3.- Code the free generation function where you will need to iterate through all of the related
//:     persons, you malloced, and release the memory used.
//:
//:


// Simulate genetic inheritance of blood type

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <cs50.h>

// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
} person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

int main(void)
{
    /// Seed random number generator
    srand(time(0));

    /// Create a new family with three generations
    person *p = create_family(GENERATIONS);

    /// Print family tree of blood type
    print_family(p, 0);

    /// Free memory
    free_family(p);
}

// Create a new individual with `generations`
person *create_family(int generations)
{
    //| TODO: Allocate memory for new person
    /// Create the new person
    person *person_ptr = malloc(sizeof(person));


    // If there are still generations left to create
    if (generations > 1)
    {
        // Create two new parents for current person by recursively calling create_family
        person *mamae = create_family(generations - 1);
        person *papae = create_family(generations - 1);

        //| TODO: Set parent pointers for current person
        person_ptr->parents[0] = mamae;
        person_ptr->parents[1] = papae;

        //| TODO: Randomly assign current person's alleles based on the alleles of their parents
        if ((rand() % 2) == 0)
        {
            ///  We will use the left alleles
             person_ptr->alleles[0] = mamae->alleles[0];
             person_ptr->alleles[1] = papae->alleles[0];
        }
        else
        {
             person_ptr->alleles[0] = mamae->alleles[1];
             person_ptr->alleles[1] = papae->alleles[1];
        }


    }

    // If there are no generations left to create
    else
    {
        /// This is the base case.  There are no parents here
        person_ptr->parents[0] = NULL;
        person_ptr->parents[1] = NULL;
        person_ptr->alleles[0] = random_allele();
        person_ptr->alleles[1] = random_allele();
    }

    //| TODO: Return newly created person

    return person_ptr;
}

// Free `p` and all ancestors of `p`.
void free_family(person *p)
{
    //| TODO: Handle base case
    /// If the person has no parents, we can go ahead and delete it and exit
    if (p == NULL)
    {
        return;
    }

    //| TODO: Free parents recursively
    person *mamae = p->parents[0];
    person *papae = p->parents[1];
    free_family(mamae);
    free_family(papae);

    free(p);
    //| TODO: Free child
}

// Print each family member and their alleles.
void print_family(person *p, int generation)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print person
    if (generation == 0)
    {
        printf("Child (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else if (generation == 1)
    {
        printf("Parent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else
    {
        for (int i = 0; i < generation - 2; i++)
        {
            printf("Great-");
        }
        printf("Grandparent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }

    // Print parents of current generation
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

// Randomly chooses a blood type allele.
char random_allele()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
