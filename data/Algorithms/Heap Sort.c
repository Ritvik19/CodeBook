#include <stdlib.h>
#include <stdio.h>

void heapify(int arr[], int n, int i)
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    int temp;

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

    if (largest != i)
    {
        temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    int temp;
    for (int i = n - 1; i >= 0; i--)
    {
        temp = arr[i];
        arr[i] = arr[0];
        arr[0] = temp;
        heapify(arr, i, 0);
    }
}

int main()
{
    int i, arr[10], arr_size;
    printf("Implementation of Heap Sort\n");
    printf("Number of Elements?  ");
    scanf("%d", &arr_size);
    printf("Enter Elements\n");
    for (i = 0; i < arr_size; i++)
        scanf("%d", &arr[i]);

    printf("Elements are\n");
    for (i = 0; i < arr_size; i++)
        printf("%d  ", arr[i]);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    for (i = 0; i < arr_size; i++)
        printf("%d  ", arr[i]);

    return 0;
}
