def LinearSearch(arr,key):
    isFound=False
    for i in range(len(arr)):
        if key == arr[i]:
            isFound=True
            print("Element found at index {}".format(i))
    if not(isFound):
        print("Element is not present in the array")  
        
n=int(input("Enter the number of elements: "))
arr=list(map(int,input().strip().split()))
key=int(input("Enter the element you are searching for: "))
LinearSearch(arr,key)

