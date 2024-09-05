# delimiter

if __name__ == '__main__':
    s = 'anh.duy!tran?dep!trai.nhat.the#gioi'
    delim = '.?!#'
    for x in delim:
        s=s.replace(x,'')
    print(s.split())

# So nguyen lon

if __name__ == '__main__':
    s = input()

    tong  = 0
    for x in s:
        tong += int(x)
    print(tong)


