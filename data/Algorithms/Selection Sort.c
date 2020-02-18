#include <stdio.h>
#include <conio.h>

int *iselection_sort(int data[], int length)
{
    int i, j, min, temp;
    for (i = 0; i < length - 1; i++)
    {
        min = i;
        for (j = i + 1; j < length; j++)
            if (data[j] < data[min])
                min = j;
        temp = data[min];
        data[min] = data[i];
        data[i] = temp;
    }
    return &data[0];
}
int *dselection_sort(int data[], int length)
{
    int i, j, min, temp;
    for (i = 0; i < length - 1; i++)
    {
        min = i;
        for (j = i + 1; j < length; j++)
            if (data[j] > data[min])
                min = j;
        temp = data[min];
        data[min] = data[i];
        data[i] = temp;
    }
    return &data[0];
}

void main()
{
    clrscr();
    int data[10], n, i, choice, *ptr;
    printf("Selection Sorting\n");

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
        ptr = iselection_sort(data, n);
    else if (choice == 2)
        ptr = dselection_sort(data, n);

    for (i = 0; i < n; i++)
    {
        printf("%d  ", *ptr);
        ptr++;
    }
    getch();
}
