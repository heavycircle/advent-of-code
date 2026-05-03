#include <ctype.h>
#include <search.h> // This might be cheating ...
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TARGET "a"

char *strip(char *str)
{
    size_t len = strlen(str);
    if (!len)
        return str;
    char *end = str + len - 1;

    // Trim ending chars
    while (end >= str && isspace(*end))
        --end;
    *(end + 1) = '\0';

    // Trim start chars
    while (*str && isspace(*str))
        ++str;

    return str;
}

long hash_get(char *key)
{
    // Check for literals
    char *endptr;
    long num = strtol(key, &endptr, 10);
    if (*key != '\0' && *endptr == '\0')
        return num & 0xffff;

    // Check the hash table
    ENTRY *ep = hsearch((ENTRY) { .key = key }, FIND);
    if (ep != NULL)
        return (long)ep->data & 0xffff;

    // Could not resolve
    return -1;
}

void hash_set(char *key, long val)
{
    ENTRY e = { .key = strdup(key), .data = (void *)val };

    if (hsearch(e, ENTER) == NULL)
    {
        fprintf(stderr, "hash_set: failed: key='%s' val=%ld\n", key, val);
        exit(1);
    }
}

void do_line(char *op, char *res)
{
    char *tokens[3];
    long lhs, rhs;

    tokens[0] = strtok(op, " ");
    tokens[1] = strtok(NULL, " ");

    // Assignment
    if (tokens[1] == NULL)
    {
        if ((lhs = hash_get(tokens[0])) == -1)
            return;
        hash_set(res, lhs);
        return;
    }

    // NOT
    if (strcmp(tokens[0], "NOT") == 0)
    {
        if ((lhs = hash_get(tokens[1])) == -1)
            return;
        hash_set(res, ~lhs);
        return;
    }

    // TWO ops
    tokens[2] = strtok(NULL, " ");
    if ((lhs = hash_get(tokens[0])) == -1)
        return;
    if ((rhs = hash_get(tokens[2])) == -1)
        return;

    if (strcmp(tokens[1], "AND") == 0)
        hash_set(res, lhs & rhs);
    else if (strcmp(tokens[1], "OR") == 0)
        hash_set(res, lhs | rhs);
    else if (strcmp(tokens[1], "LSHIFT") == 0)
        hash_set(res, lhs << rhs);
    else if (strcmp(tokens[1], "RSHIFT") == 0)
        hash_set(res, lhs >> rhs);
}

long process_file(char *file, char *init_key, long init_val)
{
    // Lazily not validating here ...
    FILE *fp = fopen(file, "r");
    if (fp == NULL)
    {
        perror("fopen");
        exit(1);
    }

    hcreate(26 * 26);
    if (init_key != NULL)
        hash_set(init_key, init_val);

    char *line = NULL;
    size_t cap = 0;

    long res;
    while ((res = hash_get(TARGET)) == -1)
    {
        rewind(fp);

        while (getline(&line, &cap, fp) > 0)
        {
            char *copy = strdup(line);
            char *op = strip(strtok(copy, "->"));
            char *res = strip(strtok(NULL, "->"));

            if (hash_get(res) == -1)
                do_line(op, res);

            free(copy);
        }
    }

    free(line);
    hdestroy();
    fclose(fp);

    return res;
}

int main(int argc, char *argv[])
{
    long one = process_file(argv[1], NULL, 0);
    printf("ONE: %ld\n", one);

    long two = process_file(argv[1], "b", one);
    printf("TWO: %ld\n", two);

    return 0;
}
