from collections import Counter
from math import*
from sys import stdin

def check(n):
    r = n % 10
    n //= 10
    while n!= 0 :
        if r < n % 10:
            return False
        r = n % 10
        n //= 10
    return True

if __name__ == '__main__':
    d = dict({})
    for line in stdin:
        a = list(map(int,line.split()))
        for x in a:
            if check(x):
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
    d = list(d.items())