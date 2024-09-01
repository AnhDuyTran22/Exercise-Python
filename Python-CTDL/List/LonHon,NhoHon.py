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
    x = int(input())
    lon,nho = 0,0
    for item in a:
        if item < x:
            nho +=1
        elif item > x :
                lon +=1
    print(nho,lon,sep='\n')
    