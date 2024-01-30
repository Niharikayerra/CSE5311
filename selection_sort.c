#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void selection_sort(int arr[], int n)
{
    int i, j, temp, minindex;
    for(i=0; i<n-1; i++)
    {
        minindex = i;
        for(j=i+1; j<n; j++)
        {
            if(arr[j] < arr[minindex])
            {
                minindex = j;
            }
        }
        if(minindex != i)
        {
            temp = arr[i];
            arr[i] = arr[minindex];
            arr[minindex] = temp;
        }
    }
}
int main()
{
    int n, i;
    srand(time(0));
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Random numbers generated: ");
    for(i=0; i<n; i++)
    {
        arr[i] = rand() % 1000;
        printf("%d ", arr[i]);
    }
    printf("\n");
    selection_sort(arr,n);
    printf("Sorted Array is: ");
    for(i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}