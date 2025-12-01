#define _GNU_SOURCE
#include "aoclib.h"

#include <ctype.h>
#include <libgen.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

/**********************************************
 *  LOGGERS                                   *
 *********************************************/

void sprint(const char **a, size_t n)
{
    for (size_t i = 0; i < n; ++i)
        printf("%s ", a[i]);
    printf("\n");
}

void dprint(const int *a, size_t n)
{
    for (size_t i = 0; i < n; ++i)
        printf("%d ", a[i]);
    printf("\n");
}

void lprint(const long *a, size_t n)
{
    for (size_t i = 0; i < n; ++i)
        printf("%ld ", a[i]);
    printf("\n");
}

void fprint(const double *a, size_t n)
{
    for (size_t i = 0; i < n; ++i)
        printf("%f ", a[i]);
    printf("\n");
}

/**********************************************
 *  UTILITIES                                 *
 *********************************************/

char *strip(char *str)
{
    // Strip leading whitespace
    while (isspace(*str))
        ++str;

    // Strip trailing whitespace
    char *end = str + strlen(str) - 1;
    while (end > str && isspace(*end))
        --end;
    *(end + 1) = '\0';

    // Return stripped string
    return str;
}

char **split(const char *str, const char *delim, size_t *len)
{
    // Make copy
    char *copy = strdup(str);
    if (!str)
        return NULL;

    // Get number of instances
    size_t num = 1, idx = 0;
    char *tmp = copy, *ptr;
    while (*tmp)
    {
        if (strstr(tmp, delim) == tmp)
        {
            ++num;
            tmp += strlen(delim);
        }
        else
        {
            ++tmp;
        }
    }

    // Generate list
    char **list = calloc(num, sizeof(char *));
    if (!list)
        return NULL;

    // Get tokens
    char *token = strtok_r(copy, delim, &ptr);
    while (token != NULL)
    {
        list[idx++] = token;
        token = strtok_r(NULL, delim, &ptr);
    }

    // Return list
    if (len)
        *len = idx;
    return list;
}

char **readlines(FILE *fp, size_t *len)
{
    // Get number of lines
    size_t num = 0;
    char *line = NULL;
    size_t dummy;
    while (getline(&line, &dummy, fp) != -1)
        ++num;
    fseek(fp, 0, 0);

    char **lines = calloc(num, sizeof(char *));
    for (size_t i = 0; i < num; ++i)
    {
        getline(&line, &dummy, fp);
        lines[i] = strdup(line);
    }
    if (len)
        *len = num;
    return lines;
}

int index_of(const char *str, char c)
{
    const char *l = strchr(str, c);
    return l != NULL ? (l - str) : -1;
}

int *rev_array(int *arr, size_t len)
{
    for (size_t i = 0; i < len / 2; ++i)
    {
        const int tmp = arr[i];
        arr[i] = arr[len - i - 1];
        arr[len - i - 1] = tmp;
    }
    return arr;
}

char *replace(const char *s, char a, char b)
{
    char *ret = strdup(s);
    for (size_t i = 0; i < strlen(s); ++i)
        if (s[i] == a)
            ret[i] = b;
    return ret;
}

long gcd(long a, long b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

long lcm(const long a[], size_t n)
{
    long ans = a[0];
    for (size_t i = 1; i < n; ++i)
        ans = (((a[i] * ans)) / (gcd(a[i], ans)));
    return ans;
}

int *intify(char **a, size_t n)
{
    int *r = calloc(n, sizeof(int));
    for (size_t i = 0; i < n; ++i)
        r[i] = atoi(a[i]);
    free(a);
    return r;
}

long *longify(char **a, size_t n)
{
    long *r = calloc(n, sizeof(long));
    for (size_t i = 0; i < n; ++i)
        r[i] = atol(a[i]);
    free(a);
    return r;
}

/**********************************************
 *  MAIN METHODS                              *
 *********************************************/

FILE *get_datafile(size_t year, size_t day)
{
    // Get the executable path
    char *root = calloc(PATH_MAX, sizeof(char));
    ssize_t len = readlink("/proc/self/exe", root, PATH_MAX - 1);
    root[len] = 0;

    // Walk up checking for sentinel files
    while (1)
    {
        // Check if we're at root
        if (strcmp(root, "/") == 0)
        {
            fprintf(stderr, "get_data: could not find project root\n");
            free(root);
            exit(-1);
        }

        // Get the absolute path
        char *sentinel = NULL;
        if (asprintf(&sentinel, "%s/.git", root) < 0)
        {
            fprintf(stderr, "get_data: out of memory\n");
            free(root);
            exit(-1);
        }

        // Check the sentinels
        struct stat st;
        if (stat(sentinel, &st) == 0 && S_ISDIR(st.st_mode))
        {
            LOG("info", "get_data: found sentinel: .git");
            free(sentinel);
            break;
        }

        // Go up one
        free(sentinel);
        root = dirname(root);
    }

    // Add the input file path
    char path[PATH_MAX] = { 0 };
    snprintf(path, PATH_MAX - 1, "%s/input/%zu/day-%02zu.txt", root, year, day);
    LOG("info", "get_data: found input: %s", path);
    free(root);

    // Get this file
    FILE *fp = fopen(path, "r");
    if (!fp)
    {
        fprintf(stderr, "get_data: input file missing\n");
        exit(-2);
    }

    return fp;
}

char *get_data(size_t year, size_t day)
{
    // Get file pointer. Will exit if bad.
    FILE *fp = get_datafile(year, day);

    // Get file size
    fseek(fp, 0, SEEK_END);
    size_t size = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    // Allocate this much memory
    char *data = calloc(size, sizeof(char));
    if (!data)
    {
        fprintf(stderr, "get_data: out of memory\n");
        fclose(fp);
        exit(-1);
    }

    // Copy memory
    size_t rec = fread(data, sizeof(char), size, fp);
    if (rec != size)
    {
        fprintf(stderr, "get_data: couldn't read entire file\n");
        fclose(fp);
        exit(-1);
    }

    fclose(fp);
    return data;
}
