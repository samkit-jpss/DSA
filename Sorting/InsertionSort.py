def InsertionSort(arr):
    for i in range(1,len(arr)):
        position = i 
        current_value = arr[i]
        while position>0 and arr[position-1] > current_value:
            arr[position] = arr[position-1]
            position = position-1

        arr[position] = current_value
    print(arr)

InsertionSort([3,6,2,14,5,1])    