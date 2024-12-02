//.*************************************************************************************************
//. User Story:
//.*************************************************************************************************
/// There are many situations where you’ll find it helpful to have a function that finds the maximum
/// (and minimum) value in an array. Since there is no built-in max function in C, you’ll create
/// one in this practice problem. You can then use it in upcoming problem sets where it may be
/// helpful!
///
///


//.*************************************************************************************************
//. Requirements:
//.*************************************************************************************************
/// 1.- Start out with a variable that keeps track of your max value. There are two ways to
///     initialize this. You can start out using the lowest possible value (be careful you don’t
///     start with zero, as the max value could be a negative number!) or you can start with the
///     first element in the array.
///
/// 2.- Loop through the array and reset this max value every time you find a value that’s larger.
///
/// 3.- Respond with "The max value is"
///
/// 4.- The main function initializes the array, asks the user to enter values, and then passes the
///     array and the number of items to the max function. Complete the max function by iterating
///     through every element in the array, and return the maximum value.


// Practice writing a function to find a max value

#include <cs50.h>
#include <stdio.h>

int max(int array[], int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        arr[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(arr, n));
}

// TODO: return the max value
int max(int array[], int n)
{
    int max_value = -2147483648;
    for (int i = 0; i < n; i++)
    {
        printf("The number is [%i]\n", array[i]);
        if (array[i] > max_value)
        {
            max_value = array[i];
        }
    }
    return max_value;
}
