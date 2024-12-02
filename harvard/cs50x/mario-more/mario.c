#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    int leftSpaces = 0;
    for (int i = 0; i < height; i++)
    {
        leftSpaces = ((height - 1) - i);
        // printf("On iteration %i, the number of spaces is %i\n", i, leftSpaces);
        for (int j = 0;j < leftSpaces; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < (i + 1); k++)
        {
            printf("#");
        }
        printf("  ");
        for (int k = 0; k < (i + 1); k++)
        {
            printf("#");
        }
        printf("\n");
    }

}


