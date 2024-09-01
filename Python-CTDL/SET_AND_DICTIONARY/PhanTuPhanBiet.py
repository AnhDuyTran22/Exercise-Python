from collections import  Counter

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    print(len(set(a)))