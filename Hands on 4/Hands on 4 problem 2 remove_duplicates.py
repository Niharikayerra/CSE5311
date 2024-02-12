def remove_duplicates(arr):
    j=0
    for i in range (0,len(arr)-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j+=1
    arr[j] = arr[-1]
    return arr[:j+1]
print("Enter the array:")
arr = list(map(int, input().split()))
result = remove_duplicates(arr)
print("Array after removing duplicates:")
print(result)        