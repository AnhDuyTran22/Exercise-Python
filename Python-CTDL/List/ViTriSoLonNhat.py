from math import*

def nt(n):
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    min_val,max_val = min(a),max(a)
    min_pos , max_pos = 0,0
    for i in range(n):
        if a[i] == min_val:
            min_pos = i
    for i in range(n):
        if a[i] == max_val:
            max_pos = i
            break
    print(max_pos,min_pos)