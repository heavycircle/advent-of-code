#include <aoclib.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    int *ptr;
    size_t len;
} List;

int cmp_int(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int main(void)
{
    char *data = get_data(2024, 1);
    if (!data)
    {
        fprintf(stderr, "Could not get data from AOC\n");
        exit(EXIT_FAILURE);
    }

    // Count number of newlines
    char *s = data;
    int i = 0;
    for (; s[i]; s[i] == '\n' ? ++i : *s++)
        ;

    // Lists for the pairs
    List x = { .ptr = calloc(i, sizeof(int)), .len = i };
    List y = { .ptr = calloc(i, sizeof(int)), .len = i };

    // Fill the lists
    i = 0;
    s = data;
    while (*s)
    {
        int l, r, n = 0;
        if (sscanf(s, "%d %d%n", &l, &r, &n) == 2)
        {
            x.ptr[i] = l;
            y.ptr[i] = r;
            ++i;
            s += n;
        }
        else
        {
            break;
        }
    }

    // Sort
    qsort(x.ptr, x.len, sizeof(int), cmp_int);
    qsort(y.ptr, y.len, sizeof(int), cmp_int);

    // Get differences
    int one = 0, two = 0;
    for (size_t i = 0; i < x.len; ++i)
    {
        one += abs(y.ptr[i] - x.ptr[i]);
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
