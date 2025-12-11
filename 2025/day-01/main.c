#include <stdio.h>
#include <stdlib.h>

#define LOCK_LEN 100

int rotate(int *cur, char *rot)
{
    int tmp = *cur;
    long l = strtol(rot + 1, NULL, 10);
    int pass = (int)l / LOCK_LEN;
    int left = (int)l % LOCK_LEN;

    // Minimal rotation
    if (rot[0] == 'L')
        *cur -= (int)left;
    else if (rot[0] == 'R')
        *cur += (int)left;

    if (*cur == 0)
        ++pass;

    // Out of bounds correction
    if (*cur >= LOCK_LEN || *cur < 0)
    {
        if (tmp != 0)
            ++pass;

        *cur %= LOCK_LEN;
        if (*cur < 0) // C's modulus keeps the sign of the dividend
            *cur += LOCK_LEN;
    }

    return pass;
}

int main(void)
{
    FILE *fp = fopen("real.txt", "r");

    char *line = NULL;
    size_t len;

    int start = 50;
    int one = 0, two = 0;
    while (getline(&line, &len, fp) != -1)
    {
        two += rotate(&start, line);
        if (start == 0)
            ++one;
    }

    printf("ONE: %d\n", one);
    printf("TWO: %d\n", two);

    if (line)
        free(line);
    fclose(fp);
    return 0;
}
