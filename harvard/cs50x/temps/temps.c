// Practice working with structs
// Practice applying sorting algorithms

#include <cs50.h>
#include <stdio.h>
#include <string.h>

#define NUM_CITIES 10

typedef struct
{
    string city;
    int temp;
}
avg_temp;

avg_temp temps[NUM_CITIES];

void sort_cities(void);

int main(void)
{
    temps[0].city = "Austin";
    temps[0].temp = 97;

    temps[1].city = "Boston";
    temps[1].temp = 82;

    temps[2].city = "Chicago";
    temps[2].temp = 85;

    temps[3].city = "Denver";
    temps[3].temp = 90;

    temps[4].city = "Las Vegas";
    temps[4].temp = 105;

    temps[5].city = "Los Angeles";
    temps[5].temp = 82;

    temps[6].city = "Miami";
    temps[6].temp = 97;

    temps[7].city = "New York";
    temps[7].temp = 85;

    temps[8].city = "Phoenix";
    temps[8].temp = 107;

    temps[9].city = "San Francisco";
    temps[9].temp = 66;
/*
    temps[0].city = "Austin";
    temps[0].temp = 10;

    temps[1].city = "Boston";
    temps[1].temp = 9;

    temps[2].city = "Chicago";
    temps[2].temp = 8;

    temps[3].city = "Denver";
    temps[3].temp = 7;

    temps[4].city = "Las Vegas";
    temps[4].temp = 6;

    temps[5].city = "Los Angeles";
    temps[5].temp = 5;

    temps[6].city = "Miami";
    temps[6].temp = 4;

    temps[7].city = "New York";
    temps[7].temp = 3;

    temps[8].city = "Phoenix";
    temps[8].temp = 2;

    temps[9].city = "San Francisco";
    temps[9].temp = 1;
*/
    sort_cities();

    printf("\nAverage July Temperatures by City\n\n");

    for (int i = 0; i < NUM_CITIES; i++)
    {
        printf("%s: %i\n", temps[i].city, temps[i].temp);
    }
}

// TODO: Sort cities by temperature in descending order
void sort_cities(void)
{
    /// I am going to try bubble sort first, then linear
    bool unsorted = true, at_least_one = false;
    int limit = 10;
    avg_temp wip_temps[NUM_CITIES];

    /// Copying the structure arrays
    for (int i = 0; i < NUM_CITIES; i++)
    {
        wip_temps[i].city = temps[i].city;
        wip_temps[i].temp = temps[i].temp;
    }

    printf("First city is [%s]\n", wip_temps[0].city);

    /// Now we need to iterate through the array by 2 at a time and skip the ones
    /// that have already been sorted.
    int current = 0, next = 0;
    avg_temp clipboard;
    while (unsorted)
    {
        at_least_one = false;
        for (int i = 0; i < limit; i++)
        {
            current = i;
            next = current + 1;
            if (next == limit)
            {
                continue;
            }
            if (wip_temps[current].temp > wip_temps[next].temp)
            {
                /// copy next to clipboard
                clipboard.city = wip_temps[next].city;
                clipboard.temp = wip_temps[next].temp;

                /// copy current to next
                wip_temps[next].city = wip_temps[current].city;
                wip_temps[next].temp = wip_temps[current].temp;

                /// copy clipboard to current
                wip_temps[current].city = clipboard.city;
                wip_temps[current].temp = clipboard.temp;

                at_least_one = true;
            }
        }
        if (!at_least_one)
        {
            unsorted = false;
        }
        limit -= 1;
    }
    memcpy(temps, wip_temps, sizeof(avg_temp) * 10);
}
