#include <aoclib.h>
#include <stdio.h>

int main(void)
{
    // Get the date. Function kills if non-existent.
    FILE *fp = get_data(2025, 2);

    fclose(fp);
    return 0;
}
