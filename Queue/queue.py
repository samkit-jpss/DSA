class Queue:

    def __init__(self):
        self.items=[]
    
    #Insertion of Element 
    def Enqueue(self,data):
        self.items.insert(0,data)
    
    #Pop the element at the last or first inserted element
    def Dequeue(self):
        return self.items.pop()

    #Returns the size of the list 
    def qsize(self):
        return "Length of items: {}".format(len(self.items))

   #Function that returns boolean if the list is empy or not 
    def isEmpty(self):
        return self.items == []  

weekdays=Queue() 
weekdays.Enqueue("Monday")  #inserting element "Monday"
weekdays.Enqueue("Tuesday") #inserting element "Tuesday"
weekdays.Enqueue("Wednesday") #inserting element "Wednesday"
print(weekdays.Dequeue())       #Removes "Monday"
print(weekdays.Dequeue())       #Removes "Tuesday"
print(weekdays.__dict__)        #Output what remains in the items list 
print(weekdays.qsize())          
print(weekdays.isEmpty())       