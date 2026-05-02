#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

uint64_t best(const char *line, uint64_t start, uint64_t end)
{
    uint64_t idx = 0;
    for (uint64_t i = start; i <= end; ++i)
    {
        if (line[idx] < line[i])
            idx = i;
    }
    return idx;
}

uint64_t process(const char *line, uint64_t len, uint64_t digits, uint64_t acc)
{
    if (digits == 0)
        return acc;

    int call = best(line, 0, len - digits);
    int val = line[call] - '0';
    return process(line + call + 1, len - call - 1, digits - 1, (acc * 10) + val);
}

int main(int argc, char *argv[])
{
    FILE *fp = fopen(argv[1], "r");
    uint64_t ONE = 0, TWO = 0;

    char *line = NULL;
    size_t cap = 0;
    ssize_t len = 0;
    while ((len = getline(&line, &cap, fp)) > 0)
    {
        ONE += process(line, len - 1, 2, 0);
        TWO += process(line, len - 1, 12, 0);
    }

    printf("ONE: %ld\n", ONE);
    printf("TWO: %ld\n", TWO);

    if (line)
        free(line);
    fclose(fp);
    return 0;
}
