def merge(arr1, arr2):
    merged = []
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged.append(arr1[i])
        i+=1
    while j<len(arr2):
        merged.append(arr2[j])
        j+=1
    return merged
def mergekarrays(arrays):
    merged = arrays[0]
    for arr in arrays[1:]:
        merged = merge(merged, arr)
    return merged
k = int(input("Enter the number of arrays:"))
n = int(input("Enter the size of array:"))
arrays = []
for i in range(k):
    print(f"Enter the elements for array{i+1}:")
    arr = list(map(int, input().split()))
    arrays.append(arr)
merged_array = mergekarrays(arrays)
print("Merged array is:",merged_array)