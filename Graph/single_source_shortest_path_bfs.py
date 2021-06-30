class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            self.gdict = {}
        self.gdict = gdict
      
    def spp_bfs(self,start,end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path 
            for adjacent_vertex in self.gdict.get(node):
                    new_path = list(path)
                    new_path.append(adjacent_vertex)
                    queue.append(new_path)
                
my_airport = {
    "jaipur":["mumbai","delhi"],
    "mumbai":["chennai","kerala"],
    "delhi":["chennai","gujrat"],
    "chennai":["jammu"],
    "gujrat": ["jammu"],
    "jammu":["kerala"]
    
}


print(obj.spp_bfs("delhi","kerala"))

# The output should be ['delhi', 'chennai', 'jammu', 'kerala']
