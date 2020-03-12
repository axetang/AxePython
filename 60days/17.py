# Day 17：Python 列表生成式高效使用的 12 个案例
# Python 里使用 [] 创建一个列表。容器类型的数据进行运算和操作，生成新的列表最高效的办法——列表生成式。

from math import floor
import os
from random import random
a = range(0, 11)
b = [x**2 for x in a]
print(b)
c = [str(x) for x in a]
print(c)

a = [round(random(), 2) for _ in range(10)]
print(a)

a = range(11)
d = [x**2 for x in a if x % 2 == 0]
print(d)

a = [i*j for i in range(1, 10) for j in range(1, i+1)]
print(a)


a = range(5)
print(a)
b = ['a', 'b', 'c', 'd', 'e']
c = [str(y)+str(x) for x, y in zip(a, b)]
x = zip(a, b)
print(type(x), x)
print(c)


a = {'a': 1, 'b': 2, 'c': 3}
# b = [k+'='+v for k, v in a.items()]
b = [k+'='+str(v) for k, v in a.items()]
print(b)

a = [d for d in os.listdir("./")]
print(a)
dirs = [d for d in os.listdir("./") if os.path.isdir(d)]
print(dirs)

fs = [f for f in os.listdir("./") if os.path.isfile(f)]
print(fs)

a = ["Hello", "World", "AXe", 2020]
b = [str(w).lower() for w in a]
print(b)
c = [w.lower() for w in a if isinstance(w, str)]
print(c)


def filter_non_unique(lst):
    return [item for item in lst if lst.count(item) == 1]


uni = filter_non_unique([1, 2, 3, 3, 5, 8, 1, 6, 9, 2, 4, 6])
print(uni)


def bifurcate(lst, filter):
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False]

    ]


bif = bifurcate(['beep', 'boop', 'bar', 'foo'], [True, True, False, True])
print(bif)


def bifurcate_by(lst, fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]


bif_by = bifurcate_by(
    ['Python3', 'up', 'users', 'people'], lambda x: x[0] == 'u')
print(bif_by)


def difference(a, b):
    _a, _b = set(a), set(b)
    return [item for item in _a if item not in _b]


dif = difference([1, 1, 2, 3, 3], [1, 2, 4])
print(dif)

# from math import floor


def difference_by(a, b, fn):
    _b = set(map(fn, b))
    print("type(map(fn,b)) is ", type(map(fn, b)), map(fn, b))
    print("type(_b) is ", type(_b), "_b:", _b)
    return [item for item in a if fn(item)not in _b]


dif_by = difference_by([2.1, 1.2], [2.3, 3.4], floor)
print(dif_by)
dif_by = difference_by([{'x': 2}, {'x': 1}], [{'x': 1}], lambda v: v['x'])
print(dif_by)
