if __name__ == '__main__':
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int,input().split()))
        a.append(b)
    min_val , max_val = 10**18,-10**18
    for i in range(n):
        for j in range(m):
            min_val = min(min_val,a[i][j])
            max_val = max(max_val,a[i][j])

    print(min_val,max_val)




