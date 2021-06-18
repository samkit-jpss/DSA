class Graph:
    def __init__(self,gdict=None):
        self.gdict = gdict
    def addConn(self,vertex,conn):
        self.gdict[vertex].append(conn)
    def connectionsLenght(self,vertex):
        return len(self.gdict[vertex])
    def addVertex(self,vertex):
        self.gdict[vertex]=[]

connections ={"samkti" : ["nehal","vidhisha","vidhi","akhilesh"],
"nehal" : ["samkit","anuj"],
"anuj" : ["samkit"],
             }

obj1 = Graph(connections)
