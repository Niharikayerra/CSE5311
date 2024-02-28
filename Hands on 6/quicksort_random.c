#include<stdio.h>
#include<stdlib.h>
#include<time.h> 
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
int choosePivot(int low, int high)
{
    return low + rand() % (high - low + 1);
}
int partition(int arr[], int low, int high)
{
    int pivotIndex = choosePivot(low,high);
    int pivot = arr[pivotIndex];
    swap(&arr[pivotIndex], &arr[high]);
    int i = low-1;
    for(int j = low; j<high; j++)
    {
        if(arr[j]<=pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[high]);
    return i+1;
}
void quicksort(int arr[], int low, int high)
{
    if(low<high)
    {
        int pivotIndex = partition(arr, low, high);
        quicksort(arr, low, pivotIndex-1);
        quicksort(arr, pivotIndex+1, high);
    }
}
int main()
{
    int arr[] = {4, 8, 2, 5, 1, 9, 7, 0};
    int n = sizeof(arr)/sizeof(arr[0]);
    srand(time(NULL));
    printf("Original array is: ");
    for(int i=0; i<n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    quicksort(arr, 0, n-1);
    printf("The Sorted Array is: ");
    for(int i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}