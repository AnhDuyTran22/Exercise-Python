from functools import cmp_to_key

if __name__ == '__main__':
    s = input()
    t = ''
    for x in s:
        if x.isalpha():
            t += ' '
        else:
            t += x
    a = list(map(int,t.split()))
    print(sum(a ))