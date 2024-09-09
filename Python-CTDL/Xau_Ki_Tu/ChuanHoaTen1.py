if __name__ == '__main__':
    s = input()
    a = s.split()
    print(' '.join(a).title())
    t = input()
    if t[1] == '/':
        t = '0' + t
    if t[4] == '/':
        t = t[0:3] + '0' + t[3]
    print(t)