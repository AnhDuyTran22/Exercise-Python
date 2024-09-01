def tong(n):
    ans = 0
    while n!=0:
        ans += n%10
        n//=10


if __name__ == '__main__':
    n  =int(input())
    a = list(map(int,input().split()))
    a.sort(key=lambda x : (tong(x),x))
    for x in a:
        print(x, end = ' ')