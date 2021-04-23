class SLinkedList:
    def __init__(self,data):
        self.data=data
        self.nextnode=None   

head=SLinkedList('JAN') #head node 
data2=SLinkedList('FEB') #second node  
head.nextnode=data2 #Linking head node to the next node 
data3=SLinkedList('MAR') #Third Node 
data2.nextnode=data3 #Linking second node to the third node  
data4=SLinkedList('APRIL') #Fourth Node 
data3.nextnode=data4 #Linking third node to the fourth node 

# Loop to print the data values present in the node
while head is not None:
    print(head.data)
    head=head.nextnode

#For verification if the nodes are linked to each other 
#print(data2.__dict__) #In second field we can see the address to its next node
#print(hex(id(data3))) #verify the address if its same then linked list implemented successfull (as data2 is linked to data3)

