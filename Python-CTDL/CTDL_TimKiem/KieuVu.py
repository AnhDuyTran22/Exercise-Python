if __name__ == '__main__':
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    i,j = 0,0
    cnt = 0
    while i < n and j < m:
        if a[i] > b[j]:
            cnt += 1
            i += 1
            j += 1
        else:
            i += 1
    print(cnt)