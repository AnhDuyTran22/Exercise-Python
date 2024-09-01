from math import*

def nt(n):
    if n < 2 :
        return False
    for i in range(2,isqrt(n)+1):
        if n%i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    min_val = min(a)
    dem = 0
    for x in a:
        if x == min_val:
            dem += 1
    print(dem) 