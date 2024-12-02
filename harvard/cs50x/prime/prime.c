#include <cs50.h>
#include <stdio.h>

bool prime(int number);

int main(void)
{
    int min;
    do
    {
        min = get_int("Minimum: ");
    }
    while (min < 1);

    int max;
    do
    {
        max = get_int("Maximum: ");
    }
    while (min >= max);

    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)
{
    // TODO
    // If zero, return false
    if (number == 0 || number == 1)
    {
        return false;
    }
    if (number == 2)
    {
        return true;
    }
    int counter = 2;
    do
    {
        // printf("loop number [%i] and number is [%i]\n", counter, number);
        if (number % counter == 0)
        {
            return false;
        }
        counter += 1;
    }
    while (counter < number);

    return true;
}
