def BubblesSort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                
                
    return data
            
data = [5,4,3,2,1]        
BubblesSort(data)        
        