#include <aoclib.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *data = get_data(2025, 1);
    if (!data)
    {
        fprintf(stderr, "get_data: missing input file\n");
        return 1;
    }

    free(data);
    return 0;
}
