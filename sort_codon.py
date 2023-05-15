"""
Sort an array with the requested algorithm
"""

from time import perf_counter
from random import randint
#from array import array

def merge(a, l, r, m):
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


def sort(a, l: int, r: int) -> None:
    """
    Sort a list with the requested sorting algorithm
    :param a: array of values to sort
    :param l: left boundary index - where to start sorting
    :param r: right boundary index - where to stop sorting
    :return: None
    """
    # Begin implementation
    li = l
    ri = l
    j = 0
    for i in range(l, r+1):
        j += 1
        if i == r or (a[i] > a[i+1]):
            ri = i
            if j > 1:
                merge(a, l, ri, li)
            li = ri + 1
    # End implementation


# Add your auxiliary methods here
# Begin implementation


# End implementation

numbers = 5000
expected = []
a = __array__[int](5000)
for i in range(numbers):
    number = randint(-numbers, numbers)
    a[i] = number
    expected.append(number)
start_time = perf_counter()
sort(a, 0, 4999)
sort_time = perf_counter()-start_time
print('mine ', sort_time)
start_time = perf_counter()
expected.sort()
sort_time = perf_counter()-start_time
print('reference', sort_time)

