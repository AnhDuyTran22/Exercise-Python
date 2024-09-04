from math import*

def nt(n):
    if n <  2 :
        return False
    else:
        for i in range(2,isqrt(n)+1):
            if n%i==0:
                return False
        return True



if __name__ == '__main__':
    n = int(input())
    a = []
    for  _ in range(n):
        b = list(map(int,input().split()))
        a.append(b)
    dem = 0
    s = set({})
    for i in range(n):
        if nt(a[i][i]):
            s.add(a[i][i])
        if nt(a[i][n-i-1]):
            s.add(a[i][n-i-1])
    print(len(s))