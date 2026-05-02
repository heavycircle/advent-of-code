#include <aoclib.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long solve(long nums[6], long off)
{
    // Make offsets
    long x = nums[4] + off;
    long y = nums[5] + off;

    // Get solutions
    long a = roundl((y - ((nums[3] * x) / (double)nums[2]))
        / (double)(nums[1] - ((nums[3] * nums[0]) / (double)nums[2])));
    long b = roundl((x - nums[0] * a) / (double)nums[2]);

    // Check values
    if (nums[0] * a + nums[2] * b == x && nums[1] * a + nums[3] * b == y)
        return a * 3 + b;
    else
        return 0;
}

int main(void)
{
    char *data = get_data(13, 2024);

    char *start = data, *end;
    long nums[6];
    int i;

    long one = 0, two = 0;
    while (start && start[0] && start[1])
    {
        // Button lines
        for (i = 0; i < 4; ++i)
        {
            start = strchr(start, '+');
            nums[i] = strtol(start + 1, &end, 10);
            start = end;
        }
        // Prize line
        for (i = 4; i < 6; ++i)
        {
            start = strchr(start, '=');
            nums[i] = strtol(start + 1, &end, 10);
            start = end;
        }

        // Solver
        one += solve(nums, 0);
        two += solve(nums, 10000000000000);
    }

    printf("ONE: %ld\n", one);
    printf("TWO: %ld\n", two);

    free(data);
    return EXIT_SUCCESS;
}
