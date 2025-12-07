#include <aoclib.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void parse(char *data)
{
    // Read until the line length is one
    char *line = data;
    char *end;

    while (line && *line)
    {
        // Get the line length
        end = strchr(line, '\n');
        size_t len = end ? (size_t)(end - line) : strlen(line);
        if (len <= 1)
            break;
    }
}

int main(void)
{
    char *data = get_data(5, 2024);
    parse(data);

    free(data);
    return EXIT_SUCCESS;
}
