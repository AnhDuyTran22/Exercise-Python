n,m,p = map(int,input().split())

a,b = [0]*n,[0]*m

for i in range(n):
    a[i] = list(map(int,input().split()))
for i in range(m):
    b[i] = list(map(int,input().split()))

c = [[0 for _ in range(n)] for _ in range(p)]
for i in range(n):
    for j in range(p):
        for k in range(m):
            c[i][j] += a[i][k]*b[k][j]
print(c)