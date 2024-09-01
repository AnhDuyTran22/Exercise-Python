if __name__ == '__main__':
    a = [1,3,1,3,1,4,1,0,2,5]
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
        for val,fre in d.items():
            print(val,fre)


# tra ve kieu tuple
if __name__ == '__main__':
    a = [1,3,1,3,1,4,1,0,2,5]
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    b = list(d.items())
    b.sort(key=lambda x:x[0])
    print(b)


a = [1,2,3,4]


