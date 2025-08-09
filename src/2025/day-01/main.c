#include <aoclib.h>
#include <stdio.h>

int main(void)
{
    FILE *fp = get_data(2025, 1);
    if (!fp)
    {
        fprintf(stderr, "get_data: missing input file\n");
        return 1;
    }

    fclose(fp);
    return 0;
}
