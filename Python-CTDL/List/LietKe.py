from math import*

def nt(n):
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i == 0:
            return False
    return True

def tn(n):
    temp = n
    rev = 0
    while n!= 0 :
        rev = rev*10 + n%10
        n//=10
    return temp == rev 

def cp(n):
    can =isqrt(n)
    return can*can == n

def check(n):
    tong = 0 
    while n!= 0 :
        tong += n%10
        n//=10
    return nt(tong)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    d1,d2,d3,d4 = 0,0,0,0
    for x in a:
        if nt(x):
            d1 += 1
        if tn(x):
            d2 += 1
        if cp(x):
            d3 += 1
        if check(x):
            d4 += 1
    print(d1,d2,d3,d4,sep='\n')

























