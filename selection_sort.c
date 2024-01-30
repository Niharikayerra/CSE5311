#include<stdio.h>
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
    int arr[100], n, i;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    printf("Enter %d integers: ",n);
    for(i=0; i<n; i++)
    {
        scanf("%d", &arr[i]);
    }
    selection_sort(arr,n);
    printf("Sorted Array is: ");
    for(i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}