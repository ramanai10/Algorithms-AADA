d = dict()
edg = dict()
set = dict()
p = list()
adj = dict()
s = int(0)
pred = dict()
class Dijkstra:
    def __init__(self, v):
        self.V = v

    def initialize(self, ls):
        for i in ls:
            d[i] = 9999
            adj[i] = []
            set[i] = False
            pred[i] = 0
    def initSource(self, src):
        d[src] = 0
    def add_edge(self, ed, w):
        edg[ed] = w
        p.append(ed)
        adj[ed[0]].append(ed[1])

    def printPath(self, a, b):
        if a == s or b == 0:
            print(a, end=" ")
        else:
            self.printPath(b, pred[b])
            print(a, end=" ")  
  
    def shortestPath(self,s):
        u = s
        for i in range(self.V):
            res = 999
            for j in d:
                if (res > d[j]) and (set[j] == False):
                    u = j
            for i in adj[u]:
                if d[i] > (d[u] + edg[(u,i)]):
                    d[i] = d[u] + edg[(u,i)]
                    pred[i] = u
      
    def result(self, s):
        print("Shortest distance of each node from source {} :".format(s))
        for k in d:
            print("{}: {}".format(k, d[k]))
  
        print("Shortest path of each node from source {} :".format(s))
        for i in pred:
            print("{}: ".format(i) , end = " ")
            self.printPath(i, pred[i])
            print()
    def matrixRepresentation(self):
        for i in range(self.V):
            print(i+1, end = " ")
            for j in range(self.V):
                if (i+1,j+1) in p:
                    print(edg[(i+1, j+1)], end = " ")
                else:
                    print("-", end = " ")
            print()

di = Dijkstra(5)
di.initialize([1,2,3,4,5])    
di.add_edge((1,2), 10)
di.add_edge((1,3), 3)
di.add_edge((2,3), 1)
di.add_edge((2,4), 2)
di.add_edge((3,2), 4)
di.add_edge((3,4), 8)
di.add_edge((3,5), 2)
di.add_edge((4,5), 7)
di.add_edge((5,4), 9)
di.matrixRepresentation()
s = int(input("Enter the source node:"))
di.initSource(s)
di.shortestPath(s)
di.result(s)