#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void insertion_sort(int arr[], int n)
{
    int i, temp, j;
    for (i=1; i<n; i++)
    {
        temp = arr[i];
        j = i-1;
        while(j>=0 && arr[j]>temp)
        {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = temp;
    }
}
int main()
{
    int n;
    srand(time(0));
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Random numbers generated: \n");
    for (int i=0; i<n; i++)
    {
        arr[i] = rand() % 1000000;
        printf("%d ", arr[i]);
    }
    printf("\n");
    insertion_sort(arr,n);
    printf("sorted array is: ");
    for(int i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}