import re


class Graph:
    def __init__(self):
        self.adj_list = {}

    def addVertex(self, vertex):
        if vertex  not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False

    def addEdge(self, e1,e2):
        if e1   in self.adj_list.keys() and e2 in self.adj_list.keys():
            self.adj_list[e1].append(e2)
            self.adj_list[e2].append(e1)
            return True
        return False    

    def printing(self):
        for i in self.adj_list.keys():
            print( i,self.adj_list[i])  


    def removeEdge(self,e1,e2):
        if e1 in self.adj_list.keys() and e2 in self.adj_list.keys():
            self.adj_list[e1].remove(e2)
            self.adj_list[e2].remove(e1)
            return True
        return False   

    def removeVertex(self,v):
        if v in self.adj_list.keys():
            # print(self.adj_list[v])
            # both work
            # for vertex in self.adj_list.keys():
            #     if v in self.adj_list[vertex]:
            for vertex in self.adj_list[v]:
                self.adj_list[vertex].remove(v)

            del self.adj_list[v]
            return True
        return False        











my_graph=Graph()
my_graph.addVertex("A")
my_graph.addVertex("B")
my_graph.addVertex("C")
my_graph.addVertex("D")
my_graph.addEdge("A","B")
my_graph.addEdge("A","C")
my_graph.addEdge("A","D")
my_graph.addEdge("D","B")
my_graph.addEdge("D","C")
my_graph.removeVertex("D")
#my_graph.removeEdge("C","A")

my_graph.printing()

