# Tim vi tri xuat hien cua phan tu co gia tri X trong mang da sap tang dan
def first_pos(a,l,r,x):
    res = -1
    while l <= r:
        m = (l+r)//2
        if a[m] == x:
            res = m
            r = m-1
        elif a[m] < x:
            l = m+1
        else:
            r = m-1
    return res

#Tim vi tri xuat hien cuoi cung cua phan tu co gia tri X trong mang da sap tang dan

def last_pos(a,l,r,x):
    res = -1
    while l<=r:
        m = (l+r)//2
        if a[m] == x:
            res = m
            l = m + 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res


# Tim vi tri xuat hien dau tien cua phan tu cos gia tri >=X trong mang sap xep tang dan
def first_pos1(a,l,r,x):
    res = -1
    while l <=r :
        m = (l+r)//2
        if a[m] >= x:
            res = m
            r = m-1
        else:
            l = m+1
    return res


# Tim vi tri xuat hien dau tien cua phan tu co gia tri > X trong mang da sap tang dan

def first_pos2(a,l,r,x):
    res = -1
    while l<=r:
        m = (l+r)//2
        if a[m] > x:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res 



if __name__ == '__main__':
    a = [1,2,2,2,2,4,5,6]
    print(first_pos(a,0,len(a)-1,2))
    print(last_pos(a,0,len(a)-1,2))
    print(first_pos1(a,0,len(a)-1,2))
    print(first_pos2(a,0,len(a)-1,2))

