from functools import cmp_to_key

from math import*

def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i == 0:
            return False
    return True

def check(s):
    t = s[::-1]
    return s == t and '6' in s

if __name__ == '__main__':
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')