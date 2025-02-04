def insertion_sort(arr):
    unsorted = []
    answer = []
    for n in arr:
        unsorted.append(n)
        for i in range(1, len(unsorted)):
            anchor = unsorted[i]
            j = i - 1
            while j >= 0 and anchor < unsorted[j]:
                unsorted[j + 1] = unsorted[j]
                j = j - 1
            unsorted[j + 1] = anchor
            
        middle = len(unsorted)/2
        if len(unsorted) % 2 == 0:
            middle = round(middle)
            mediana = (unsorted[middle] + unsorted[middle-1]) /2
            answer.append(mediana)
        else:
            answer.append(unsorted[int(middle)])
    return answer
            
         


if __name__ == "__main__":
    arr = [2, 1, 5, 7, 2, 0, 5]

    insertion_sort(arr)
    print(insertion_sort(arr))
