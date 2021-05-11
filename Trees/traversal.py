class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        
root = TreeNode("Drinks")
hot_drinks = TreeNode("Hot Drinks")
cold_drinks = TreeNode("Cold Drinks")        
root.leftChild = hot_drinks
root.rightChild = cold_drinks

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot_drinks.leftChild=tea
hot_drinks.rightChild=coffee

thumbs_up = TreeNode("Thumbs Up")
sprite = TreeNode("Sprite")
cold_drinks.leftChild=thumbs_up
cold_drinks.rightChild=sprite

#pre-order traversal
def pre_order(mytree):
    if not mytree:
        return  
    print(mytree.data,end="->")
    pre_order(mytree.leftChild)
    pre_order(mytree.rightChild)
 
#post-order traversal
def post_order(mytree):
    if not mytree:
        return  
    pre_order(mytree.leftChild)
    pre_order(mytree.rightChild)
    print(mytree.data,end="->")
 

#In-order traversal
def in_order(mytree):
    if not mytree:
        return  
    pre_order(mytree.leftChild)
    print(mytree.data,end="->")
    pre_order(mytree.rightChild)
    
pre_order(root)
print()
post_order(root)
print()
in_order(root)    