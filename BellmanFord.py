edg = dict()
dist = dict()
color = dict()
pred = dict()
p = dict()
ls_edge = list()
class Bellman:
    def __init__(self, v):
        self.vertex = v

    def append(self, e, wt):
        edg[e] = wt
        p[e[0]].append(e[1])
        ls_edge.append(e)

    def initialize(self, d):
        for i in d:
            color[i] = 'W' #White Color
            pred[i] = 0
            dist[i] = 9999
            p[i] = []
        dist[1] = 0
        color[1] = 'G' #Gray color

    def relax_edges(self):
        n = self.vertex - 1
        for j in range(n):
            for l in ls_edge:
                a = l[0]
                b = l[1]
                if (dist[a] + edg[l]) < dist[b]:
                    dist[b] = dist[a] + edg[l]

    def result(self):
        print("Shortest distance of each node from source {} to destination {}:".format(1, 7))
        for k in dist:
            print("{}: {}".format(k, dist[k]))

    def initQueue(self):
        self.head = 0
        self.tail = 0
        self.q = list()

    def enqueue(self, x):
        self.q.append(x)
        if self.tail + 1 == len(self.q):
            self.tail = 0
        else:
            self.tail = len(self.q) - 1
   
    def dequeue(self):
        if self.head == len(self.q):
            print("No more elements to delete")
            return None
        else:
            x = self.q[self.head]
            self.q.pop(self.head)
            return x

    def printPath(self, a, b):
        if a == 1:
            print(a, end=" ")
        else:
            self.printPath(b, pred[b])
            print(a, end=" ")    
    def bfs_path(self, x):
        self.enqueue(x)
        while(len(self.q) != 0):
            u = self.dequeue()
            for i in p[u]:
                if (color[i] == 'W') and (dist[u] + edg[(u,i)] == dist[i]):
                    color[i] = 'G'
                    pred[i] = u
                    self.enqueue(i)
            color[u] = 'B' #Black color: visited node
        print("The shortest path from source {} to destination {}".format(1,7)) 
        for i in pred:
            print("{}: ".format(i) , end = " ")
            self.printPath(i, pred[i])
            print()
    
b1 = Bellman(7)
b1.initialize([1, 2, 3, 4, 5, 6, 7])
b1.append((1,2),6)
b1.append((1,3),5)
b1.append((1,4),5)
b1.append((2,5),-1)
b1.append((3,2),-2)
b1.append((3,5),1)
b1.append((4,3),-2)
b1.append((4,6),-1)
b1.append((5,7),3)
b1.append((6,7),3)
b1.relax_edges()
b1.initQueue()
b1.result()
b1.bfs_path(1)