n = int(input("Enter the number of items:"))
print("Enter the profit of the items:")
p = list(map(int, input().split()[:n]))
print("Enter the weight of the items:")
w = list(map(int, input().split()[:n]))
m = int(input("Enter the max weight:"))
c = [[0 for w in range(m + 1)] for r in range(n + 1)] 
it = list()
for i in range(0, n+1):
    print(i, end=" ")
    for j in range(0, m+1):
        if i==0 or j==0:
            c[i][j] = 0
        elif w[i-1] <= j and i>0:
            c[i][j] = max(p[i-1]+c[i-1][j-w[i-1]], c[i-1][j])
        else:
            if w[i-1] > j:
                c[i][j] = c[i-1][j]
        print(c[i][j],sep=" ",end=" ")
    print()

res = c[n][m]
print("Maximum possible weight is {}".format(res))
r = n
co = m
while r>=0:
    a = c[r][co]
    b = c[r-1][co]
    if a!=b:
        if r not in it:
            it.append(r)
        co = co - w[r-1]
        r = r - 1
    else:
        r = r - 1

print("Items: {}".format(it))