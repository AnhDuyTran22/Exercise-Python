if __name__ == '__main__':
    a = int(input())
    x = list(map(int,input().split()))
    x.sort()
    ans = 10**18
    for i in range (1,x):
        ans = min(ans,a[i] - a[i-1])
    print(ans)