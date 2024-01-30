#include<stdio.h>
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
    printf("Enter the number of elements: ",n);
    scanf("%d",&n);
    int arr[n];
    printf("Enter %d integers: ",n);
    for (int i=0; i<n; i++)
    {
        scanf("%d", &arr[i]);
    }
    bubble_sort(arr,n);
    printf("sorted array is: ");
    for(int i=0; i<n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    return 0;
}
        