from math import*
def nt(n):
    if n < 2:
        return False
    else :
        for i in range(2,isqrt(n)+1):
            if(n%i==0):
                return False
        return True
    

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(map(int,input().split()))
        a.append(b)
    dem = 0
    for i in range(n):
        if nt(a[i][i]):
            dem += 1
        if nt(a[i][n - i - 1]):
            dem += 1
    if n%2 == 1:
        if nt(a[n//2][n//2]):
            dem -= 1
    print(dem)