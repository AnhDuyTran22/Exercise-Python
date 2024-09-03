if __name__ == '__main__':
    n,l = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = max(a[0]-0,l-a[-1])
    for i in range(1,n):
        ans = max(ans,(a[i] - a[i-1])/2)
    print('%.10f' % ans)


# DRAGON 

if __name__ == '__main__':
    n,s = map(int,input().split())
    a = []
    for _ in range(n):
        b = list(map(int,input().split()))
        a.append(b)
    a.sort(key=lambda x : x[0])
    for x ,y in a:
        if x >= s:
            print('NO')
            exit()
        s += y
    print('YES')