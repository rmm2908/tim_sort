from array import array


def sort(a: array, l: int, r: int) -> None:
    li = l
    ri = l
    j = 0
    for i in range(l, r+1):
        j += 1
        if i == r or (a[i] > a[i+1]):
            ri = i
            if j > 1:
                merge(a, l, ri, li)
            ri += 1
            li = ri


def merge(a: array, l, r, m):
    helper = []
    j = 0
    ll = l
    rl = m
    l_f = False
    r_f = False
    for i in range(l, r+1):
        if ll == m and not l_f:
            l_f = True
        if rl > r and not r_f:
            r_f = True
        if l_f and r_f:
            break
        if l_f:
            helper.append(a[rl])
            rl += 1
        elif r_f:
            helper.append(a[ll])
            ll += 1
        else:
            if a[ll] <= a[rl]:
                helper.append(a[ll])
                ll += 1
            else:
                helper.append(a[rl])
                rl += 1

    for i in range(l, r+1):
        a[i] = helper[j]
        j += 1
