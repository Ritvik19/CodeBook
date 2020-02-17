#include <stdio.h>
#define N 10

// Method 1 (Recursive)
int main(int num)
{
    if (num <= N && printf("%d ", num) && main(num + 1)) {}
}

// Method 2 (Iterative)
int main(int num, char *argv[])
{
    while (num <= N && printf("%d ", num) && num++) {}
}