if __name__ == '__main__':
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int,input().split()))
        a.append(b)
    print(a)
#  VD 2,3
#     1 2 3
#     4 5 6
#     [[1, 2, 3], [4, 5, 6]]


if __name__ == '__main__':
    n,m = map(int,input().split())
    a = [[0 for _ in range(m) for _ in range(n)]]
    print(a)



if __name__ == '__main__':
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int,input().split()))
        a.append(b)
    for j in range(m):
        print(a[i][j],end=' ')
    print()























