if __name__ == '__main__':
    s = input()
    d = dict({})
    for x in s:
        if x in d:
            d[x] += 1
        else: d[x] = 1
    for kitu in sorted(d):
        print(kitu,d[kitu])
    print()
    for x,y in d.items():
        print(x,y) 