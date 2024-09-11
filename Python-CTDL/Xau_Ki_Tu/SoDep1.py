
from functools import cmp_to_key
from math import*
def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

def check(s):
    tong  = 0
    for x in s:
        tong += int(x)
        if x not in '2357':
            return False
    return nt(tong)

if __name__ == '__main__':
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')