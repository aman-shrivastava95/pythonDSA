# this version is also correct, here we are returning the new array formed, alternate could be 
# that we create small arrays, and modify the orginal array itself
def mergeSortInternal(left, right, arr):
    if left >= right:
        return [arr[left]]
    
    temp = [-1] * (right - left + 1)
    mid = left + (right - left)//2
    arr1 = mergeSortInternal(left, mid, arr)
    arr2 = mergeSortInternal(mid + 1, right, arr)

    #combine both arr1 and arr2 
    n1 = len(arr1)
    n2 = len(arr2)
    i = j = k = 0
    while j < n1 and k < n2:
        if arr1[j] < arr2[k]:
            temp[i] = arr1[j]
            j+=1
        else:
            temp[i] = arr2[k]
            k+=1
        i+=1

    #check if anything is remaining in any of the two arrays
    while j < n1:
        temp[i] = arr1[j]
        j+=1
        i+=1
    
    while k < n2:
        temp[i] = arr2[k]
        k+=1
        i+=1
    return temp
   

def mergeSort(arr):
    left = 0 ;
    right = len(arr) - 1

    return mergeSortInternal(left, right, arr);

arr = [9,8,7,6,5,4,3,2,1]
sorted_arr = mergeSort(arr)
print(sorted_arr)
