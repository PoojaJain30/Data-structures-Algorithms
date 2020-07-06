#Implement Graph
class Graph:
    
    def __init__(self):
        self.nodeNumbers = 0
        self.adjacentList = {}
        
    def __str__(self):
        return str(self.__dict__)
    
    def addNodes(self,node):
        self.adjacentList[node] = []
        self.nodeNumbers += 1
        return self.adjacentList
    
    def addEdges(self,nod1,nod2):
        self.adjacentList[nod1].append(nod2)
        self.adjacentList[nod2].append(nod1)
        return self.adjacentList
    
my_Graph = Graph()
my_Graph.addNodes('o')
my_Graph.addNodes('p')
my_Graph.addEdges('o','p')
