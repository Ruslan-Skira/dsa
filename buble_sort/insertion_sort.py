def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]
        internal = i
        while list_a[internal - 1] > value_to_sort and internal > 0:
            list_a[internal], list_a[internal - 1] = list_a[internal - 1], list_a[internal]
            internal = internal - 1
    return list_a


print(insertion_sort([1,5, 33, 3, 22, 21]))



def ins_sert(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1
            
            
і   