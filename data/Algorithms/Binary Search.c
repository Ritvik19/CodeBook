#include <stdio.h>
#include <conio.h>

int b_search(int data[], int length, int item)
{
    int first = 0, last = length - 1, mid, i = 0;
    while (first <= last)
    {
        i++;
        printf("%d Iteration performed\n", i);
        mid = (first + last) / 2;
        if (item > data[mid])
            first = mid + 1;
        else if (item < data[mid])
            last = mid - 1;
        else
            return mid;
    }
    return -1;
}

void main()
{
    clrscr();
    int data[10], i, n, item;
    printf("Implementation of Binary Search\n");

    printf("Enter number of elements (max 10) ");
    scanf("%d", &n);

    printf("Enter elements\n");
    for (i = 0; i < n; i++)
        scanf("%d", &data[i]);

    printf("Enter item to be searched ");
    scanf("%d", &item);

    int found = b_search(data, n, item)

        if (found == -1)
            printf("Item Not Found");
    else printf("Item Found At Index %d", found);

    getch();
}
