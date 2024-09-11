from functools import cmp_to_key


# C1
if __name__ == '__main__':
    s = input()
    tong = 0
    for x in s:
        tong += int(x)
    print(tong)


# C2
if __name__ == '__main__':
    s = list(input())
    s = [int(x) for x in s]
    print(sum(s))