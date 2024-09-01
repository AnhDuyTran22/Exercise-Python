from math import*

def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    dem,tong = 0,0
    for x in a:
        if nt(x):
            dem += 1
            tong += x
    print('%.2f' %(tong/dem))