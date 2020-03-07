# 1. update
# 实际使用字典时，需要批量插入键值对到已有字典中，
# 使用 update 方法实现批量插入。已有字典中批量插入键值对：
from collections import ChainMap
d = {'a': 1, 'b': 2}
d.update({'c': 3, 'd': 4, 'e': 5})
print(d)
d.update([('f', 6), ('g', 7)])
print(d)
d.update([('h', 8), ('i', 9)], j=10)
print(d)

# 2. setdefault
# 如果仅当字典中不存在某个键值对时，才插入到字典中；
# 如果存在，不必插入（也就不会修改键值对）。
# 这种场景，使用字典自带方法 setdefault
d = {'a': 1, 'b': 2}
d.setdefault('c', 3)
print(d)
d.setdefault('c', 4)
print(d)


# 3. 字典并集
# 先来看这个函数 f，为了好理解，显示的给出参数类型、返回值类型，这不是必须的。
print("*/**")


def f(d: dict) -> dict:
    return {**d}


def merge(d1, d2):
    return {**d1, **d2}


def merge1star(d1, *d2):
    return [d1, *d2]


def merge2star(d1, **d2):
    return {**d1, **d2}


print(f({'a': 1, 'b': 2}))
print(merge({'a': 1, 'b': 2}, {'c': 3}))
print(merge1star(5, 6, 7, 8))
print(merge2star({'a': 1, 'b': 2}, c=3, d=4))


def difference(d1, d2):
    # 4. 字典差
    return dict([(k, v) for k, v in d1.items() if k not in d2])


d = difference({'a': 1, 'b': 2, 'c': 3}, {'b': 2})
print('字典差：', d)
# 使用dict函数，以元组为列表元素，构建字典。注意不可以以列表为列表元素来构建
d = dict([('a', 3), ('b', 4), ('c', 5)])
print(d)


# 5. 按键-按值排序

def sort_by_key(d):
    return sorted(d.items(), key=lambda x: x[0])


def sort_by_value(d):
    return sorted(d.items(), key=lambda x: x[1])


d = {'a': 3, 'x': 1, 'c': 2, 'b': 5, 'r': 10}
print(d.items())
print("sorted d by key:", sort_by_key(d))
print("sorted d by value:", sort_by_value(d))
print("origin d: ", d)
# [('a', 3), ('b', 1), ('c', 2)]

# 7. 最大键、最大值


def max_key(d):
    if len(d) == 0:
        return []
    max_key = max(d.keys())
    return (max_key, d[max_key])


def max_value(d):
    if len(d) == 0:
        return []
    max_value = max(d.values())
    return [(key, max_value) for key in d if d[key] == max_value]


d = {'a': 3, 'c': 5, 'd': 10, 'b': 3, 'e': 10}
t = max_key(d)
print(t)
l = max_value(d)
print(l)


def max_min(s):
    # 9. 集合最值:找出集合中的最大、最小值，并装到元组中返回：
    return (max(s), min(s))


def single(string):
    # 10. 单字符串: 若组成字符串的所有字符仅出现一次，则被称为单字符串。
    return len(set(string)) == len(string)


print(max_min({1, 3, 5, 7}))
print(single('love_python'))  # False
print(single('python'))  # True
print(single('felixx'))  # True


def longer_shorter(s1, s2, ls):
    # 11. 更长集合:key 函数定义为按照元素长度比较大小，找到更长的集合：
    if ls == 'longer':
        return max(s1, s2, key=lambda x: len(x))
    elif ls == 'shorter':
        return min(s1, s2, key=lambda x: len(x))
    else:
        return 'Wrong command!'


print(longer_shorter({1, 3, 5, 7}, {1, 5, 7}, 'longer'))  # {1,3,5,7}
print(longer_shorter({1, 3, 5, 7}, {1, 5, 7}, 'shorter'))  # {1,3,5,7}
print(longer_shorter({1, 3, 5, 7}, {1, 5, 7}, 'xxx'))  # {1,3,5,7}


# 12. 重复最多: 在两个列表中，找出重叠次数最多的元素。默认只返回一个。
def max_overlap(lst1, lst2):
    overlap = set(lst1).intersection(lst2)
    ox = [(x, min(lst1.count(x), lst2.count(x))) for x in overlap]
    return max(ox, key=lambda x: x[1])


max_overlap([1, 2, 2, 2, 3, 3], [2, 2, 3, 2, 2, 3])


"""
13. topn 键

找出字典前 n 个最大值，对应的键。

导入 Python 内置模块 heapq 中的 nlargest 函数，获取字典中的前 n 个最大值。

key 函数定义按值比较大小：

In [82]: from heapq import nlargest

In [83]: def topn_dict(d, n):
    ...:     return nlargest(n, d, key=lambda k: d[k])

In [84]: topn_dict({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3)
Out[84]: ['a', 'd', 'c']
14. 一键对多值字典

一键对多个值的实现方法 1，按照常规思路，循序渐进：

In [85]: d = {}
    ...: lst = [(1,'apple'),(2,'orange'),(1,'compute')]
    ...: for k,v in lst:
    ...:     if k not in d:
    ...:         d[k]=[]
    ...:     d[k].append(v)

In [86]: d
Out[86]: {1: ['apple', 'compute'], 2: ['orange']}
以上方法，有一处 if 判断 ，确认 k 是不是已经在返回结果字典 d 中。

不是很优雅！

可以使用 collections 模块中的 defaultdict，它能创建属于某个类型的自带初始值的字典。使用起来更加方便：

In [87]: from collections import defaultdict
    ...:
    ...: d = defaultdict(list)
    ...: for k,v in lst:
    ...:     d[k].append(v)

In [88]: d
Out[88]: defaultdict(list, {1: ['apple', 'compute'], 2: ['orange']})
"""
# 15. 逻辑上合并字典
# 案例 3 中合并字典的方法：
dic1 = {'x': 1, 'y': 2}
dic2 = {'y': 3, 'z': 4}
merged = {**dic1, **dic2}
print("**", merged)
# 修改 merged['x']=10，dic1 中的 x 值不变，merged 是重新生成的一个“新字典”。

# 但是，collections 模块中的 ChainMap 函数却不同，它在内部创建了一个容纳这些字典的列表。
# 使用 ChainMap 合并字典，修改 merged['x']=10 后，dic1 中的 x 值改变。如下所示：
#from collections import ChainMap
dic1 = {'x': 1, 'y': 2}
dic2 = {'y': 3, 'z': 4}

print("dic1:", dic1)  # 改变，共用内存的结果
merged = ChainMap(dic1, dic2)
print(merged)
merged['x'] = 10
print("dic1:", dic1)  # 改变，共用内存的结果
