#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, arr[1000], i;
    scanf("%d", &num);
    for (i = 0; i < num; i++)
    {
        scanf("%d", &arr[num - i - 1]);
    }

    /* Write the logic to reverse the array. */

    for (i = 0; i < num; i++)
        printf("%d ", arr[i]);
    return 0;
}
