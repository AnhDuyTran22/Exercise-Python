if __name__ == '__main__':
    t = input().lower()
    s = input().lower()
    a = set(s.split())
    b = set(t.split())
    khac = a.difference(b)
    print(''.join(sorted(khac)))