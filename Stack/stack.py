class Stack:
    #creating an empty stack 
    def __init__(self):
        self.stk=[]
    #function to push the data
    def push(self,data):
        self.stk.append(data)
    # function to pop the data
    def pop(self):
        return self.stk.pop()
    #To check wheter the stack is empty or not
    def isEmpty(self):
        if self.stk == None:
            return "Stack is Empty"
        else:
            return "Stack is not Empty"         
    

plates = Stack()

plates.push("Plate A")
plates.push("Plate B")
plates.push("Plate C")   

plates.pop()

print(plates.isEmpty())