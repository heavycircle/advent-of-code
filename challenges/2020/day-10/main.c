#include <stdio.h>
#include <stdlib.h>

// In-place, error-checking wrapper for realloc.
void resize_long(long **arr, size_t new_len)
{
    void *tmp = reallocarray(*arr, new_len, sizeof(long));
    if (arr == NULL)
    {
        perror("realloc");
        exit(1);
    }

    *arr = tmp;
}

// Comparison for longs
int cmp_long(const void *a, const void *b)
{
    return *(long *)a - *(long *)b;
}

long do_one(const long *arr, size_t len)
{
    // Pre-account for first (always 1) and last (always 3).
    // Use 4-array to avoid doing an if-check.
    size_t diffs[4] = { 0, 1, 0, 1 };

    for (size_t i = 0; i < len - 1; ++i)
        diffs[arr[i + 1] - arr[i]] += 1;
    return (long)(diffs[1] * diffs[3]);
}

long do_two(const long *arr, size_t len)
{
    long max = arr[len - 1];
    unsigned long long *ways = calloc(max + 1, sizeof(unsigned long long));
    if (ways == NULL)
    {
        perror("calloc");
        exit(1);
    }
    ways[0] = 1; // Guaranteed to reach 0 somehow.

    long item;
    for (int i = 0; i < len; ++i)
    {
        item = arr[i];
        if (item == 0)
            continue;

        if (item - 1 >= 0)
            ways[item] += ways[item - 1];
        if (item - 2 >= 0)
            ways[item] += ways[item - 2];
        if (item - 3 >= 0)
            ways[item] += ways[item - 3];
    }

    return ways[max];
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        exit(1);
    }

    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        perror("fopen");
        exit(1);
    }

    long *arr = calloc(1, sizeof(long));

    char *line = NULL;
    size_t cap = 0;

    size_t i = 0;
    while (getline(&line, &cap, fp) > 0)
    {
        resize_long(&arr, i + 1);
        arr[i++] = strtol(line, NULL, 10);
    }
    qsort(arr, i, sizeof(long), cmp_long);

    printf("ONE: %ld\n", do_one(arr, i));
    printf("TWO: %ld\n", do_two(arr, i));

    free(arr);
    free(line);
    fclose(fp);

    return 0;
}
