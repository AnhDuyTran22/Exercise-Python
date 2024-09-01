from math import*

def nt(n):
    if n < 2 :
        return True
    else:
        for i in range(2,isqrt(n)+1):
            if n%i == 0:
                return False
        return True
    
F = [0]*100

def ktao():
    F[0] = 0
    F[1] = 1
    for i in range(2,100):
        F[i] = F[i-1] + F[i-2]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    ktao()
    check = False
    for x in a:
        if x in F:
            print(x,end=' ')
            check = True
    if not check:
        print('NONE')

        