#include<stdio.h>
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low-1;
    for(int j=low; j<high; j++)
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

int quickselect(int arr[], int low, int high, int i)
{
    if(low==high)
    {
        return arr[low];
    }
    int pivotindex = partition(arr,low,high);
    int k =  pivotindex - low +1;
    if(i==k)
    {
        return arr[pivotindex];
    }
    else if(i<k)
    {
         return quickselect(arr,low,pivotindex-1,i);
    }
    else
    {
        return quickselect(arr, pivotindex+1,high,i-k);
    }
}
int ith_order_statistic(int arr[], int n, int i)
{
    if(i<0 || i>=n)
       return -1;
    return quickselect(arr, 0, n-1,i);
}

int main()
{
    int arr[] = {4,2,5,1,8,0,7,6};
    int n = sizeof(arr)/sizeof(arr[0]);
    int i=3;
    int result = ith_order_statistic(arr,n,i);
    printf("The %dth order statistic is: %d\n",i, result);
    return 0; 
}