#include "advent.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    int   *ptr;
    size_t len;
} List;

int cmp_int(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int main(void)
{
    char *data = get_data(1, 2024);
    if (!data)
    {
        fprintf(stderr, "Could not get data from AOC\n");
        exit(EXIT_FAILURE);
    }

    // Count number of newlines
    char *s = data;
    int   i = 0;
    for (; s[i]; s[i] == '\n' ? ++i : *s++)
        ;

    // Lists for the pairs
    List x = { .ptr = calloc(i, sizeof(int)), .len = i };
    List y = { .ptr = calloc(i, sizeof(int)), .len = i };

    // Realloc necessities
    char *save, *split;

    // First item
    split    = strtok_r(data, " ", &save);
    x.ptr[0] = (int)strtol(split, NULL, 10);

    // Action the rest
    bool left = false;
    i         = 0;
    while ((size_t)i < x.len)
    {
        if (left)
        {
            split = strtok_r(NULL, " ", &save);
            if (!split)
                break;
            long l     = strtol(split, NULL, 10);
            x.ptr[i++] = (int)l;
        }
        else
        {
            split = strtok_r(NULL, "\n", &save);
            if (!split)
                break;
            long l     = strtol(split, NULL, 10);
            y.ptr[i++] = (int)l;
        }

        // Invert flag parity
        left = !left;
    }

    // Sort
    qsort(x.ptr, x.len, sizeof(int), cmp_int);
    qsort(y.ptr, y.len, sizeof(int), cmp_int);

    // Get differences
    int one = 0, two = 0;
    for (size_t i = 0; i < x.len; ++i)
    {
        one += (y.ptr[i] - x.ptr[i]);
        for (size_t j = 0; j < y.len; ++j)
        {
            if (x.ptr[i] == y.ptr[j])
                two += x.ptr[i];
        }
    }

    printf("ONE: %d\n", one);
    printf("TWO: %d\n", two);

    free(x.ptr);
    free(y.ptr);
    free(data);

    return EXIT_SUCCESS;
}
