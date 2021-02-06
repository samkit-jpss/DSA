def BinarySearch(data,key):
    start=0
    end=len(data)-1
    middle=int((start+end)/2)
    while not(data[middle] == key):
        middle=int((start+end)/2)  
        if key>data[middle]:
            start = middle + 1
        if key not in data:
            print("Element is not present in data")
            break
        else:
            end = middle-1
    if data[middle] == key:
        print("Element {} found at index {}".format(key,middle))          

BinarySearch([1,2,3,4,5,6,7,8,9,11,14],5)