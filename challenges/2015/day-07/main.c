#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TARGET "a"

typedef struct node
{
    char *key;
    long data;
    struct node *next;
} node_t;

node_t *map;

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

    // Check the map
    node_t *ptr = map;
    while (ptr != NULL)
    {
        if (strcmp(ptr->key, key) == 0)
            return ptr->data & 0xffff;
        ptr = ptr->next;
    }

    // Could not resolve
    return -1;
}

void hash_set(char *key, long val)
{
    node_t *tmp = calloc(1, sizeof(node_t));
    tmp->key = strdup(key);
    tmp->data = val;

    // Base case
    if (map == NULL)
    {
        map = tmp;
        return;
    }

    // End case
    node_t *ptr = map;
    while (ptr->next != NULL)
        ptr = ptr->next;
    ptr->next = tmp;
}

void hash_free(void)
{
    if (map == NULL)
        return;

    node_t *tmp = map;
    while (tmp != NULL)
    {
        map = tmp->next;
        free(tmp->key);
        free(tmp);
        tmp = map;
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
    FILE *fp = fopen(file, "r");
    if (fp == NULL)
    {
        perror("fopen");
        exit(1);
    }

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

    hash_free();
    free(line);
    fclose(fp);

    return res;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        exit(1);
    }

    long one = process_file(argv[1], NULL, 0);
    printf("ONE: %ld\n", one);

    long two = process_file(argv[1], "b", one);
    printf("TWO: %ld\n", two);

    return 0;
}
