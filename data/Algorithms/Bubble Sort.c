#include <stdio.h>
#include <conio.h>

int *ibubble_sort(int data[], int length)
{
    for (int i = 0; i < length - 1; i++)
        for (int j = 0; j < length - i - 1; j++)
            if (data[j] > data[j + 1])
            {
                data[j] += data[j + 1];
                data[j + 1] = data[j] - data[j + 1];
                data[j] -= data[j + 1];
            }
    return &data[0];
}
int *dbubble_sort(int data[], int length)
{
    for (int i = 0; i < length - 1; i++)
        for (int j = 0; j < length - i - 1; j++)
            if (data[j] < data[j + 1])
            {
                data[j] += data[j + 1];
                data[j + 1] = data[j] - data[j + 1];
                data[j] -= data[j + 1];
            }
    return &data[0];
}

void main()
{
    clrscr();
    int data[10], n, i, choice, *ptr;
    printf("Bubble Sorting\n");

    printf("Enter number of elements (max 10) ");
    scanf("%d", &n);

    printf("Enter elements\n");
    for (i = 0; i < n; i++)
        scanf("%d", &data[i]);

    printf("Press 1 to sort in ascending order\n");
    printf("Press 2 to sort in descending order\n");
    printf("Choice  ");
    scanf("%d", &choice);

    if (choice == 1)
        ptr = ibubble_sort(data, n);
    else if (choice == 2)
        ptr = dbubble_sort(data, n);

    for (i = 0; i < n; i++)
    {
        printf("%d  ", *ptr);
        ptr++;
    }
    getch();
}
