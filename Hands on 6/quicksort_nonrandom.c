#include<stdio.h>
#include<stdlib.h>
void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
int partition(int arr[], int low, int high)
{
    int pivot = arr[low];
    int i = low+1;
    int j = high;
    while(1)
    {
        while(i<=j && arr[i]<=pivot)
        i++;
        while(i<=j && arr[j]>=pivot)
        j--;
        if(i<=j)
        {
            swap(&arr[i], &arr[j]);
        }
        else
        {
            break;
        }
    }
    swap(&arr[low], &arr[j]);
    return j;
}
void quicksort(int arr[], int low, int high)
{
    if (low<high)
    {
        int pivotIndex = partition(arr, low,high);
        quicksort(arr, low, pivotIndex-1);
        quicksort(arr, pivotIndex+1, high);
    }
}
int main()
{
    int arr[] = {4, 8, 2, 5, 1, 9, 7, 0};
    int n = sizeof(arr)/sizeof(arr[0]);
    printf("Original Array is: ");
    for(int i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    quicksort(arr, 0, n-1);
    printf("Sorted Array is: ");
    for(int i=0; i<n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    return 0;
}
