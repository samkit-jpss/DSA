class Queue:
    def __init__(self):
        self.items=[]
    def Enqueue(self,data):
        self.items.insert(0,data)
    def Dequeue(self):
        return self.items.pop()
    def qsize(self):
        return "Length of items: {}".format(len(self.items))
weekdays=Queue() 
weekdays.Enqueue("Monday")
weekdays.Enqueue("Tuesday")
weekdays.Enqueue("Wednesday")
print(weekdays.Dequeue())
print(weekdays.Dequeue())
print(weekdays.__dict__)
print(weekdays.qsize())