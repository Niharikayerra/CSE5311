#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void bubble_sort(int arr[], int n)
{
    for(int i=0; i<n-1; i++)
    {
        for (int j=0; j<n-i-1; j++)
        {
            if(arr[j]>arr[j+1])
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
int main()
{
    int n;
    srand(time(0));
    printf("Enter the number of elements: ",n);
    scanf("%d",&n);
    int arr[n];
    printf("Random Numbers generated: \n");
    for (int i=0; i<n; i++)
    {
        arr[i] = rand() % 10000;
        printf("%d ", arr[i]);
    }
    printf("\n");
    bubble_sort(arr,n);
    printf("sorted array is: ");
    for(int i=0; i<n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    return 0;
}
        