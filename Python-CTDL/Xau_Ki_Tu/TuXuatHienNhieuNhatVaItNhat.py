if __name__ == '__main__':
    s = input()
    a = s.split()
    d = dict({})
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    min_fre,max_fre = 10**18,0
    res1, res2 =' ',' '
    for x in sorted(d):
        if d[x] >= max_fre:
            max_fre,res1 = d[x],x
        if d[x] <= min_fre:
            min_fre,res2 = d[x],x

    print(res1,max_fre)
    print(res2,min_fre)