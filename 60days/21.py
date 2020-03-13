# Day 21：5 个常用的高阶函数，3 个创建迭代器
# 高阶函数
# filter(function, iterable)　　
# 过滤器，过滤掉不满足函数 function 的元素，重新返回一个新的迭代器。
# 这个函数大概等价于下面自定义函数 filter_self：
# filter_self 函数接收一个 function 作为参数，满足条件的元素才得以保留。


from collections.abc import Iterator
from functools import reduce


def filter_self(function, iterable):
    return iter([item for item in iterable if function(item)])


# 调用 filter_self，筛选出满足指定身高的学生。其条件是，男生身高超过 1.75，女生身高超过 1.65。
class Student():
    def __init__(self, name, sex, height):
        self.name = name
        self.sex = sex
        self.height = height


def height_condition(stu):
    if stu.sex == 'male':
        return stu.height > 1.75
    else:
        return stu.height > 1.65


students = [Student('xiaoming', 'male', 1.74),
            Student('xiaohong', 'female', 1.68),
            Student('xiaoli', 'male', 1.80)]
students_satisfy = filter_self(height_condition, students)
for stu in students_satisfy:
    print(stu.name)

stus = [Student('xm', 'male', 1.78),
        Student('xz', 'female', 1.80),
        Student('xh', 'female', 1.70),
        Student('xa', 'female', 1.80),
        Student('xb', 'male', 1.90),
        Student('xc', 'female', 1.50),
        Student('xd', 'male', 1.60),
        ]
s_satisfy = filter(height_condition, stus)
for s in s_satisfy:
    print(s.name)


# map(function, iterable, …)
# 它将 function 映射于 iterable 中的每一项，并返回一个新的迭代器。
# 如下，map 函数实现每个元素加 1：
mylst = [1, 2, 5, 3, 7, 6]
result = map(lambda x: x+1, mylst)
print(type(result), result)
print(list(result))


xy = map(lambda x, y: x % 2 == 1 and y % 2 == 0, [1, 3, 2, 4, 1], [3, 2, 1, 2])
for i in xy:
    print(i)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]


def vector_add(x, y):
    return list(map(lambda i, j: i+j, x, y))


print(vector_add(l1, l2))


# reduce(function, iterable[, initializer])
# 提到 map，就会想起 reduce，前者生成映射关系，后者实现归约。
# reduce 函数位于 functools 模块中，使用前需要先导入。
# from functools import reduce
# reduce 函数中第一个参数是函数 function。function 函数，参数个数必须为 2，
# 是可迭代对象 iterable 内的连续两项。
# 计算过程，从左侧到右侧，依次归约，直到最终为单个值并返回。
rd = reduce(lambda x, y: x+y, list(range(10)))
print(rd)

rd = reduce(lambda x, y: x*y, [1, 2, 3, 4, 5, 6])
print(rd)
# reversed(seq)
# 重新生成一个反向迭代器，对输入的序列实现反转。
nl = [1, 4, 2, 3, 1]
rev = reversed(nl)
print("nl", nl)
for i in rev:
    print(i)


# sorted(iterable, *, key=None, reverse=False)
# 实现对序列化对象的排序，不影响原iterable参数，和reversed一样
# key 参数和 reverse 参数必须为关键字参数，都可省略。

a = [1, 4, 2, 3, 1]
print(sorted(a, reverse=True))
print(a)
# 如果可迭代对象的元素也是一个复合对象，如下为字典。
# 依据为字典键的值，sorted 的 key 函数就会被用到。

a = [{'name': 'xiaoming', 'age': 20, 'gender': 'male'},
     {'name': 'xiaohong', 'age': 18, 'gender': 'female'},
     {'name': 'xiaoli', 'age': 19, 'gender': 'male'}]

b = sorted(a, key=lambda x: x['age'], reverse=False)
print(b)
c = sorted(a, key=lambda x: x['name'], reverse=False)
print(c)
c = sorted(a, key=lambda x: x['name'], reverse=True)
print(c)


# 迭代器
# iter(object[, sentinel])
# 返回一个严格意义上的可迭代对象，其中，参数 sentinel 可有可无。
lst = [1, 3, 5]
it = iter(lst)
print(it)
print(it.__next__())
print(it.__next__())
print(next(it))


# 下面的 for 和 in 结合，我们都比较熟悉，iterable 为可迭代对象，依次迭代输出元素。
# for ele in iterable:
#    print(ele)
# 对象 iterable 要想支持以上这类结构，需要满足什么条件呢？
# 只要 iterable 对象支持可迭代协议，即自定义了 __iter__ 函数，便都能配合 for 依次迭代输出其元素。
# 如下，TestIter 类实现了迭代协议，__iter__ 函数。


class TestIter(object):
    def __init__(self):
        self._lst = [1, 3, 2, 3, 4, 5]

     # 支持迭代协议(即定义有 __iter__() 函数)
    def __iter__(self):
        print("__iter__ is called!!")
        return iter(self._lst)


# 所以，对象 t 便能结合 for，迭代输出元素。
t = TestIter()
for e in t:  # 因为实现了 __iter__ 方法，所以 t 能被迭代
    print(e)


# next(iterator,[, default])
# 返回可迭代对象的下一个元素：
print("next")
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# 当迭代到最后一个元素 1 时，再执行 next，就会抛出 StopIteration，迭代器终止运行。


# 案例：定制一个递减迭代器
# 编写一个迭代器，通过循环语句，对某个正整数，依次递减 1，直到 0。
# 实现类 Descrease，继承于 Iterator 对象，重写两个方法：
#   __iter__
#   __next__
print("递减迭代器")


class Decrease(Iterator):
    def __init__(self, init):
        self.init = init

    def __iter__(self):
        return self

    def __next__(self):
        while 0 < self.init:
            self.init -= 1
            return self.init
        raise StopIteration


# 调用递减迭代器 Decrease：

descend_iter = Decrease(5)
for i in descend_iter:
    print(i)


#enumerate(iterable, start=0)　　
# enumerate 是很有用的一个内置函数，尤其要用到列表索引时。
# 它返回可枚举对象，也是一个迭代器。
s = ['a', 'b', 'c']
for i, v in enumerate(s):
    print(i, v)
enum = enumerate(s)
print(next(enum))
print(next(enum))
print(next(enum))
