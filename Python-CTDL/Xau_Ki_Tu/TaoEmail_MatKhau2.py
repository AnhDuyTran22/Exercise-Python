if __name__ == '__main__':
    n = int(input())
    d = dict({})
    for _ in range(n):
        s = input().lower()
        a = s.split()
        ns = a[-1]
        email = a[-2]
        for i in range(len(a) - 2 ):
            email += a[i][0]
        if email in d:
            d[email] += 1
            print(email,d[email],'@xyz.edu.vn',sep = '')
        else:
            d[email] = 1
            print(email + '@xyz.deu.vn')
        b = ns.split('/')
        for x in b:
            print(int(x),end = '')
        print()