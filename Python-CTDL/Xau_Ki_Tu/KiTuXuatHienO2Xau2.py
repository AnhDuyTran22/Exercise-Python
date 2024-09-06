if __name__ == '__main__':
    s = input()
    t = input()
    set1, set2 = set(s),set(t)
    res1 = set1.difference(set2)
    res2 = set2.difference(set1)
    print(''.join(sorted(res1)))
    print(''.join(sorted(res2)))