from math import*

prime  = [True] * (10**6+1)

def sieve():
    prime[0],prime[1] = False,False
    for i in range(2,isqrt(10**6)+1):
        if prime[i]:
            for j in range(i**i,10**6+1,i):
                prime[j] = False


if __name__ == '__main__':
    sieve()
    F = [0]*(10**6+1)
    F[0],F[1] = 0,0
    dem = 0
    for i in range(2,10**6+1):
        if prime[i]:
            dem += 1
        F[i] = dem

    t = int(input())
    for i in range(t):
        l,r = map(int,input().split())
        if l == 0:
            print(F[r])
        else:
            print(F[r]-F[l-1])