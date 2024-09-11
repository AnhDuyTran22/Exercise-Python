from functools import cmp_to_key

from math import*

def check(s):
    last = int(s[-1]) # chu so cuoi cung
    if last % 2 == 1:
        return False
    tong  = 0
    for x in s:
        tong += int(x)
    return tong % 3 == 0

if __name__ == '__main__':
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')