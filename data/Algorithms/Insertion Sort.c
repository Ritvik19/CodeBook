#include <stdio.h>
#include <conio.h>

int *iinsertion_sort(int data[], int length)
{
    int i, key, j;
    for (i = 1; i < length; i++)
    {
        key = data[i];
        j = i - 1;
        while (j >= 0 && data[j] > key)
        {
            data[j + 1] = data[j];
            j = j - 1;
        }
        data[j + 1] = key;
    }
    return &data[0];
}
int *dinsertion_sort(int data[], int length)
{
    int i, key, j;
    for (i = 1; i < length; i++)
    {
        key = data[i];
        j = i - 1;
        while (j >= 0 && data[j] < key)
        {
            data[j + 1] = data[j];
            j = j - 1;
        }
        data[j + 1] = key;
    }
    return &data[0];
}

void main()
{
    clrscr();
    int data[10], n, i, choice, *ptr;
    printf("Insertion Sorting\n");

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
        ptr = iinsertion_sort(data, n);
    else if (choice == 2)
        ptr = dinsertion_sort(data, n);

    for (i = 0; i < n; i++)
    {
        printf("%d  ", *ptr);
        ptr++;
    }
    getch();
}
