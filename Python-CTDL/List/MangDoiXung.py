# Cach 1

from math import*

def check(a):
    left,right = 0 , len(a) - 1
    while left <= right:
        if a[left] != a[right]:
            return False
        
        left += 1
        right -= 1

    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    if check(a):
        print('YES')
    else :
        print('NO')