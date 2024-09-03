def vitridau(a,l,r,x):
    res = -1
    while l <= r:
        m = (l+r)//2
        if a[m] == x:
            res = m
            r = m - 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res

def vitricuoi(a,l,r,x):
    res = -1
    while l <= r:
        m = (l+r)//2
        if a[m] == x:
            res = m
            l = m + 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res

def vitridaulonhonbang(a,l,r,x):
    res = -1
    while j <= r:
        m = (l+r)//2
        if a[m] >= x:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res

def vitridaulonhon(a,l,r,x):
    res = -1
    while l <= r:
        m = (l+r)//2
        if a[m] > x:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res

if __name__ == '__main__':
    n , x = map(int,input().split())
    a = list(map(int,input().split()))
