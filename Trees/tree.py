class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
    def addChild(self,child):
        self.children.append(child)
Root = TreeNode("menu",[])
Hot_drinks=TreeNode("Hot Drinks",[])
Cold_drinks=TreeNode("Cold Drinks",[])
Root.addChild(Hot_drinks)
Root.addChild(Cold_drinks)
tea=TreeNode("Tea",[])
coffee=TreeNode("Coffee",[])
sprite=TreeNode("Sprite",[])
thumbs_up=TreeNode("Thumbs Up",[])
Hot_drinks.addChild(tea)
Hot_drinks.addChild(coffee)
Cold_drinks.addChild(sprite)
Cold_drinks.addChild(thumbs_up)

#prints Hot_drinks child 
for i in Hot_drinks.children:
    print(i.data)