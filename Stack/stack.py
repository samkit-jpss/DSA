class Stack:
    #creating an empty stack 
    def __init__(self):
        self.stk=[]
    #function to push the data
    def push(self,data):
        return self.stk.append(data)
    # function to pop the data
    def pop(self):
        return self.stk.pop()
    

plates = Stack()
plates.push("Plate A")
plates.push("Plate B")
plates.push("Plate C")   

plates.pop()
