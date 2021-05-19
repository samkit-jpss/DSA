class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None 
        

root = BinarySearchTree(None)

def Insert(rootNode,InsertedValue):
    if rootNode.data == None:
        rootNode.data=InsertedValue
    elif InsertedValue<=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild =  BinarySearchTree(InsertedValue)
            print("Left child inserted :  ", rootNode.leftChild.data)
        else:
            Insert(rootNode.leftChild,InsertedValue)
            print("Left child inserted :  ", rootNode.leftChild.data)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild =  BinarySearchTree(InsertedValue)
            print("Right child inserted :  ", rootNode.rightChild.data)
        else:
            Insert(rootNode.rightChild,InsertedValue)
    return "Value Inserted!!" 


Insert(root,75)
Insert(root,60)
Insert(obj,50)
