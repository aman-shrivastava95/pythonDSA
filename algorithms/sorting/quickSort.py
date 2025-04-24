def quick_sort(arr):
   def partition(left, right, arr):
        # complete this partition algo
        i = left - 1 
        pivot = arr[right]
        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j] , arr[i]
        arr[i+1], arr[right] = arr[right], arr[i + 1]
        return i + 1

   def quick_sort_internal(left, right, arr):
        if left < right: 
            mid = partition(left, right, arr)
            quick_sort_internal(left, mid -1, arr)
            quick_sort_internal(mid + 1, right, arr)

    
   n = len(arr)
   quick_sort_internal(0, n-1, arr)



arr = [8,7,6,5,4,3,2,1]
quick_sort(arr)
print(arr)
