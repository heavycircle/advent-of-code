/**
 * AOC 2021 Day 2.
 *
 * The parts are just different enough where splitting it into a function that does each part just
 * seems weird. You'd need extra 'if' cases to handle whether you're using 'aim' or not.
 */

#include <aoclib.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get the data. Function kills if non-existent.
    FILE *fp = get_datafile(2021, 2);

    long x = 0, y = 0, aim = 0;
    size_t len = 0;
    char *line = NULL;

    while (getline(&line, &len, fp) > 0)
    {
        char *k = strtok(line, " ");
        char *vstr = strtok(NULL, " ");
        long v = (long)strtol(vstr, NULL, 10);

        if (strcmp(k, "forward") == 0)
        {
            x += v;
        }
        else if (strcmp(k, "up") == 0)
        {
            y -= v;
        }
        else if (strcmp(k, "down") == 0)
        {
            y += v;
        }
    }

    printf("ONE: %ld\n", x * y);

    // Restart for P2
    fseek(fp, 0, SEEK_SET);
    x = 0;
    y = 0;

    while (getline(&line, &len, fp) > 0)
    {
        char *k = strtok(line, " ");
        char *vstr = strtok(NULL, " ");
        long v = (long)strtol(vstr, NULL, 10);

        if (strcmp(k, "forward") == 0)
        {
            x += v;
            y += aim * v;
        }
        else if (strcmp(k, "up") == 0)
        {
            aim -= v;
        }
        else if (strcmp(k, "down") == 0)
        {
            aim += v;
        }
    }

    printf("ONE: %ld\n", x * y);

    fclose(fp);
    return 0;
}
