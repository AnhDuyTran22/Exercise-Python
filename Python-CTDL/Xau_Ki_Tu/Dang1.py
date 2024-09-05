# Tan suat xuat hien


if __name__ == '__main__':
    s = 'anh duy tran dem trai nhat the gioi'
    cnt = [0]*256
    for x in s:
        cnt[ord(x)] += 1
    for i in range(256):
        if cnt[i] != 0:
            print(chr(i),cnt[i]) 


# tan xuat theo thu tu xuat hien

if __name__ == '__main__':
    s = 'anh duy tran dem trai nhat the gioi'
    cnt = [0]*256
    for x in s:
        cnt[ord(x)] += 1
    for x in s:
        if cnt[ord(x)] != 0:
            print(x,cnt[ord(x)])
            cnt[ord(x)] = 0

# Counter
from collections import Counter

if __name__ == '__main__':
        d = dict(Counter(s)).items()
        print(d)


