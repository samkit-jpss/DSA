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

#pre oreder function to print the BST 
def preOrder(root):
    if root is None:
        return 
    print(root.data)
    preOrder(root.leftChild)
    preOrder(root.rightChild)
    
#post oreder function to print the BST 
def postOrder(root):
    if root is None:
        return
    postOrder(root.leftChild)
    postOrder(root.rightChild)    
    print(root.data)

#In order function to print the BST 
def InOrder(root):
    if root is None:
        return
    InOrder(root.leftChild)
    print(root.data)
    InOrder(root.rightChild)    
    
    
    
#function calls
Insert(root,75)
Insert(root,80)
Insert(obj,50)
preOrder(root)
postOrder(root)
InOrder(root)
