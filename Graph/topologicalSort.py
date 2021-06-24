from collections import defaultdict  #To implement graph data structure using defaultdict moduel from collections 

class Graph:
    def __init__(self,numberOfVertices):       
        #To declare number of vertices the graph has
        self.numberOfVertices=numberOfVertices
        #To create a graph using adjacency list 
        self.graph=defaultdict(list)
      
    def addEdge(self,vertex,edge):
        #To append edges to the given vertex
        self.graph[vertex].append(edge)
        
    def topologicalSortUtils(self,node,visited,stack):
        visited.append(node)
        for i in self.graph[node]:
          #Based on DFS , it checks if the node has any other node it is dependent on.
            if i not in visited:
                self.topologicalSortUtils(i,visited,stack)
        stack.insert(0,node)        
        
    def topologicalSort(self):
        visited = []
        #Using stack to store the data instead of queues.
        stack = []
        for v in list(self.graph):
            if v not in visited:
                self.topologicalSortUtils(v,visited,stack)
        print(stack)    

#Declaring the number of vertices 
obj = Graph(4)

#Concept: One of devops tools is kubernetes , henc DevOps is dependent on k8s. 
obj.addEdge("DevOps","K8s")
obj.addEdge("K8s","Docker")
obj.addEdge("MLOps","ML")
obj.addEdge("ML","python")
obj.addEdge("MLOps","DevOps")

obj.topologicalSort()


#OUTPUT SHOULD BE : ['MLOps', 'ML', 'python', 'DevOps', 'K8s', 'Docker']
