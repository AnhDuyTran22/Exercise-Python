if __name__ == '__main__':
    s = input()
    d = dict({})
    for x in s:
        if x in d:
            d[x] += 1
        else: d[x] = 1
    min_fre , max_fre = 10**18,0
    res1,res = ' ',' '
    for kitu in sorted(d):
        if d[kitu] >= max_fre:
         max_fre = d[kitu]
         res1 = kitu
        if d[kitu] <= min_fre:
            min_fre = d[kitu]
            res2 = kitu
    print(res1,max_fre)
    print(res2,min_fre)

