if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input().lower()
        a = s.split()
        ns = a[-1]
        print(a[-2],end='')
        for i in range(0,len(a)-2):
            print(a[i][0],end='')
        print('@xyz.edu.vn')
        b = ns.split('/')
        for x in b:
            print(int(x),end='')
        print()