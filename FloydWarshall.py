class Floyd:
    def __init__(self, n):
        self.n = n
        self.a = [[int(0) for i in range (n+1)]for j in range (n+1)]
        self.b = [[int(0) for p in range (n+1)]for q in range (n+1)]
        for i in range(n +1):
            for j in range(n + 1):
                if i==0 or j==0:
                    self.a[i][j] = int(0)
                    self.b[i][j] = int(0)
                elif i==j:
                    self.a[i][j] = int(0)
                    self.b[i][j] = int(0)
                else:
                    self.a[i][j] = int(999)
                    self.b[i][j] = int(999)

    def addweight(self, e, f, wt): 
        self.a[e][f] = wt
        self.b[e][f] = wt

    def compute(self):
        for k in range(1, self.n + 1):
            for i in range(1, self.n + 1):
                for j in range(1, self.n + 1):
                    self.a[i][j] = min(self.a[i][j], self.a[i][k] + self.a[k][j]) 
            self.printarr(k)
        
    def printarr(self, k):
        print("Iteration {}".format(k))
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                print(self.a[i][j], end=" ")
            print()
        print()
n = int(input("Enter the number of vertices:"))
w = Floyd(n)

edg = int(input("Enter the number of edges you want to enter:"))

print("Enter the source and destination vertex followed by their weights.")

for d in range(edg):
    a1, a2, a3 = [int(x) for x in input().split()]
    w.addweight(a1, a2, a3)

w.compute()