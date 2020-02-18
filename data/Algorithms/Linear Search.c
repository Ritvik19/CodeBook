#include <stdio.h>
#include <conio.h>

int l_search(int data[], int length, int item)
{
    for (int i = 0; i < length; i++)
    {
        printf("%d Iteration performed\n", i + 1);
        if (data[i] == item)
            return i;
    }
    return -1;
}

int main()
{
    int data[10], i, n, item;
    printf("Implementation of Linear Search\n");

    printf("Enter number of elements (max 10) ");
    scanf("%d", &n);

    printf("Enter elements\n");
    for (i = 0; i < n; i++)
        scanf("%d", &data[i]);

    printf("Enter item to be searched ");
    scanf("%d", &item);

    int found = l_search(data, n, item);

    if (found == -1)
        printf("Item Not Found");
    else
        printf("Item Found At Index %d", found);

    getch();
    return 0;
}
