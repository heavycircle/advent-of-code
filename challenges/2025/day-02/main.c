#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_chunks(const char *s, size_t len, size_t num)
{
    for (size_t i = 0; i < num; ++i)
    {
        if (strncmp(s, s + i * len, len) != 0)
            return 0;
    }

    return 1;
}

int main(void)
{
    long lo, hi;
    char s[16];

    long one = 0, two = 0;
    while (EOF != scanf("%ld-%ld,", &lo, &hi))
    {
        for (long i = lo; i <= hi; ++i)
        {
            snprintf(s, sizeof(s), "%ld", i);
            size_t len = strlen(s);
            size_t chunk;

            // Part 1
            if (len % 2 == 0)
            {
                chunk = len / 2;
                if (strncmp(s, s + chunk, chunk) == 0)
                    one += i;
            }

            // Part 2
            for (chunk = 1; chunk <= len / 2; ++chunk)
            {
                if (len % chunk != 0)
                    continue;

                size_t num = len / chunk;
                if (check_chunks(s, chunk, num))
                {
                    two += i;
                    break;
                }
            }
        }
    }

    printf("ONE: %ld\n", one);
    printf("TWO: %ld\n", two);
    return 0;
}
