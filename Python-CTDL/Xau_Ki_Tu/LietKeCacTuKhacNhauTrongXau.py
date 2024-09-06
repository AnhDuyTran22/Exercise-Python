if __name__ == '__main__':
    s = input()
    a  = s.split()
    se = sorted(set(a))
    print(' '.join(se))
    set1 = set(a)
    for x in a:
        if x in set1:
            print(x,end = ' ')
            set1.remove(x)
            