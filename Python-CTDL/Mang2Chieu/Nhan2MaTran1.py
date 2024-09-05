if __name__ == '__main__':
    n,m,p = map(int,input().split())
    a = []
    for i in range(n):
        x = list(map(int,input().split()))
        a.append(x)
    b = []
    for i in range(m):
        x = list(map(int,input().split()))
        a.append(x)
    
    c = [[0 for _ in range(p)]for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]
    
    for i in range(n):
        for j in range(p):
            print(c[i][j],end = ' ')
        print()