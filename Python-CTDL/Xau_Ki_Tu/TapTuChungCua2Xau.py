if __name__ == '__main__':
    s = input().lower()
    t = input().lower()
    a = set(s.split())
    b = set(t.split())
    giao = a.intersection(b)
    print(' '.join(sorted(giao)))