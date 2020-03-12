'''
Day 18：Python 对象间的相等性比较等使用总结
Python 中，对象相等性比较相关关键字包括 is、in，比较运算符有 ==。

    is 判断两个对象的标识号（使用id()函数检测）是否相等；
    == 用于判断值或内容是否相等，默认是基于两个对象的标识号比较。
    in 用于成员检测
也就是说，如果 a is b 为 True 且如果按照默认行为，意味着 a==b 也为 True。
'''
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a), id(b), "\na==b :", a == b, "\na is b :", a is b)
a, b = [], []
print(a is b)


a, b = {'a': [1, 2, 3]}, {'id': 'book id', 'price': 'book price'}
print(a, b)
a = b
print(a, b, id(a), id(b))
print(a is b)

print(id(None))
a = None
print(a is None, id(a))

'''
in 用于成员检测

如果元素 i 是 s 的成员，则 i in s 为 True；
若不是 s 的成员，则返回 False，也就是 i not in s 为 True。
对于字符串类型，i in s 为 True，意味着 i 是 s 的子串，也就是 s.find(i) 返回大于 - 的值。举例如下：
'''
print('ab' in 'abc')
print('abc'.find('ab'))

print('ab' in 'acb')
print('abc'.find('acb'))
# 内置的序列类型、字典类型和集合类型，都支持 in 操作
# 对于字典类型，in 操作判断 i 是否是字典的键。
print([1, 2] in[[1, 2], 3])
print([1, 2] in[1, 2, 3])
print('apple' in {'orange': 1.5, 'banana': 2.3, 'apple': 5.2})


'''
对于自定义类型，判断是否位于序列类型中，需要重写序列类型的 魔法方法 __contains__。
具体操作步骤如下：
自定义 Student 类，无特殊之处
Students 类继承 list，并重写 __contains__ 方法
根据 Student 类的 name 属性，判断某 Student 是否在 Students 序列对象中。
'''


class Student():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val


class Students(list):
    def __contains__(self, stu):
        for s in self:
            if s.name == stu.name:
                return True
        return False


print("自定义类型is的判断")
s1 = Student('xiaoming')
s2 = Student('xiaohong')

a = Students()
a.extend([s1, s2])

s3 = Student('xiaoming')
print(s3 in a)  # True

s4 = Student('xiaoli')
print(s4 in a)  # False


# == 判断值是否相等
# 对于数值型、字符串、列表、字典、集合，默认只要元素值相等，== 比较结果是 True。
print("== 判断值是否相等")
str1 = "Algorithm"
str2 = 'Algorithm'
print(str1 == str2)
a = [1, 2, 3]
b = [1, 2, 3]
print("a==b", a == b, id(a), id(b), 'a is b ', a is b)
# 注意集合set，只要元素相同，就是相等，无关顺序
a = [1, 3, 2]
b = [1, 2, 3]
print("a==b", a == b)
a = {1, 2, 3}
b = {1, 3, 2}
print('a==b', a == b)


'''
对于自定义类型，当所有属性取值完全相同的两个实例，判断 == 时，返回 False。
但是，大部分场景下，我们希望这两个对象是相等的，这样不用重复添加到列表中。
比如，判断用户是否已经登入时，只要用户所有属性与登入列表中某个用户完全一致时，就认为已经登入。
如下所示，需要重写方法 __eq__，使用 __dict__ 获取实例的所有属性。
'''

print("自定义对象的相等判断")


class SStudent():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        self._age = val

    def __eq__(self, val):
        print(self.__dict__)
        return self.__dict__ == val.__dict__


a = []
xiaoming = SStudent('xiaoming', 29)
if xiaoming not in a:
    a.append(xiaoming)

xiaohong = SStudent('xiaohong', 30)
if xiaohong not in a:
    a.append(xiaohong)

xiaoming2 = SStudent('xiaoming', 29)
if xiaoming2 == xiaoming:
    print('对象完全一致，相等')

if xiaoming2 not in a:
    print("xiaoming2 not in a")
    a.append(xiaoming2)

print(len(a))


'''
小结
今天学习了 Python 中 is、in、==：
is 比较内存地址是否相等，id 获取内存地址。
in 成员属于某个序列类型中的检测
== 判断值是否相等
'''
