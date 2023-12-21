#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for start size
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9); // Ensure the starting population is at least 9

    // Prompt for end size
    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start); // Ensure the ending population is greater than or equal to the starting population

    // Calculate the number of years required for the population to reach the end size
    int years = 0;
    while (start < end)
    {
        int born = start / 3;
        int passed_away = start / 4;
        start = start + born - passed_away;
        years++;
    }

    // Print the number of years
    printf("Years: %d\n", years);

    return 0;
}

