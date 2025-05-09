#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isInt(const char c)
{
    return c >= 0x30 && c <= 0x39;
}

int one(FILE *fp)
{
    char  *line = NULL;
    size_t len;

    int t = 0;
    while (getline(&line, &len, fp) != -1)
    {
        int l = 0, r = strlen(line) - 1;
        // Send left
        while (l != r)
        {
            if (isInt(line[l]))
                break;
            ++l;
        }
        // Send right
        while (l != r)
        {
            if (isInt(line[r]))
                break;
            --r;
        }

        t += 10 * (line[l] - '0') + (line[r] - '0');
    }
    return t;
}

typedef struct map
{
    char *first;
    char *last;
    int   i;
} map;

int first(const void *a, const void *b)
{
    return ((map *)b)->first - ((map *)a)->first;
}
int last(const void *a, const void *b)
{
    return ((map *)b)->last - ((map *)a)->last;
}

int two(FILE *fp)
{
    // Starter pack
    char  *s[9] = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    char  *line = NULL;
    size_t len;
    int    t = 0;

    while (getline(&line, &len, fp) != -1)
    {
        // Find the letters
        map *n = malloc(9 * sizeof(map));
        for (int i = 0; i < 9; ++i)
        {
            n[i]     = (map) { strstr(line, s[i]), strstr(line, s[i]), i + 1 };
            char *re = n[i].last;
            while (re != NULL)
            {
                re = strstr(n[i].last + 1, s[i]);
                if (re != NULL)
                    n[i].last = re;
            }
        }

        // Send l and s to find the numbers
        int l = 0, r = strlen(line) - 1;
        while (l != r)
        {
            if (isInt(line[l]))
                break;
            ++l;
        }
        while (l != r)
        {
            if (isInt(line[r]))
                break;
            --r;
        }

        // Get first and last
        qsort(n, 9, sizeof(map), last);
        if (l == r && !isInt(line[l]))
            r = n[0].i;
        else
            r = (&line[r] < n[0].last) ? n[0].i : line[r] - '0';
        qsort(n, 9, sizeof(map), first);
        int i = 0;
        while (n[i].first != NULL)
            ++i;
        if (n[0].first == NULL)
            l = line[l] - '0';
        else
            l = (&line[l] > n[i - 1].first) ? n[i - 1].i : line[l] - '0';

        t += (10 * l + r);
        free(n);
    }
    return t;
}

int main(void)
{
    FILE *fp = fopen("day01.txt", "r");
    if (!fp)
    {
        printf("Can't open file\n");
        return 1;
    }
    printf("ONE: %d\n", one(fp));
    fseek(fp, 0, 0);
    printf("TWO: %d\n", two(fp));

    fclose(fp);
    return 0;
}
