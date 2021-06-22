class Graph:
    def __init__(self,gdict=None):
        self.gdict = gdict
    def addConn(self,vertex,conn):
        self.gdict[vertex].append(conn)
    def connectionsLenght(self,vertex):
        return len(self.gdict[vertex])
    def addVertex(self,vertex):
        self.gdict[vertex]=[]
        
    def bfs(self,vertex):
        queue = [ vertex ]
        vis = [ vertex ]
        while queue:
            deqVertex = queue.pop(0)
            print(deqVertex)
            for adjVertex in self.gdict[deqVertex]:
                if adjVertex not in vis:
                    queue.append(adjVertex)
                    vis.append(adjVertex)        

connections ={"samkit" : ["nehal","anuj"],
"nehal" : ["samkit","anuj"],
"anuj" : ["samkit"],
             }

obj1 = Graph(connections)
