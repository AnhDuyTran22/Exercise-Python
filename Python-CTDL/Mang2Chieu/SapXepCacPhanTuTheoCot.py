if __name__ == '__main__':
    n = int(input())
    a  = []
    for _ in range(n):
        b = list(map(int , input().split()))
        a.append(b)
    b = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j] = a[j][i]
    for i in range(n):
        b[i].sort()
    # in theo cot matran b
    for i in range(n):
        for j in range(n):
            print(b[j][i],end= ' ')
        print()        