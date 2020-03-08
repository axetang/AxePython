'''
学习26 个内置函数：
    16 个 Python 内置的与类型相关的函数
    10 个与自定义类属性、方法管理相关
'''
# 变量作用域

a = 10


def parent():
    b = 20

    def son():
        c = 30  # c: local
        print(b + c)  # b: enclosing
        print(a + b + c)  # a: global
        print(min(a, b, c))  # min : built-in
        # print(d)  # 在 LEGB 四个域都未找到后，报错！

    son()


parent()

# 类型函数
# bool([x])　　测试一个对象是 True，还是 False。
# 对象不为空时为true，对象为空时为false
print(bool([0, 0, 0]))
print(bool([1, 0, 0]))
print(bool([]))
print(bool([1, 0, 1]))


# bytes([source[, encoding[, errors]]])　　
# 将一个字符串转换成字节类型：
s = "apple"
b = bytes(s, encoding='utf-8')
print(b, type(b))

# str(object='')　将字符类型、数值类型等转换为字符串类型：
i = 100
print(str(i))

# chr(i)查看十进制整数对应的 ASCII 字符：
print(chr(65))
# ord(c)查看某个 ASCII 字符对应的十进制数：
print(ord('A'))


# dict() 　　
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# 创建数据字典：
print(dict())
print(dict(a='a', b='b'))
print(dict(zip(['a', 'b'], [1, 2])))
print(dict([('a', 1), ('b', 2)]))


# object()
# 返回一个根对象，它是所有类的基类。
o = object()
print(type(o))
# 使用魔法函数 __dir__，查看 object 对象上的所有方法：
print(o.__dir__())


# int(x)　　
# int(x, base=10)，x 可能为字符串或数值，将 x 转换为一个整数。
print(int('111'))
print(int('12', 16))
# print(int('19.5', 16))# 若 x 不能转化为整数，则抛出 ValueError 异常：
# int('ws') #ValueError: invalid literal for int() with base 10: 'ws'
# float(x)　　
# 将一个字符串或整数转换为浮点数：
print(float(10))
# frozenset([iterable])　　
# 创建一个不可修改的冻结集合，一旦创建不允许增删元素。
s = frozenset([1, 23, 5, 6, 7])
print(s, type(s))
# s.add(51)
# 普通集合set允许增加、删除元素
s1 = {1, 2, 34}
s1.add(90)
s1.pop()  # 删除第一个元素
print(s1)


# list([iterable])
# 返回可变序列类型：列表。如下，集合类型转列表：
s = {1, 2, 3}
print(list(s), type(list(s)))
# list 函数还常用在可迭代类型（Iterable）转化为列表。
# 如下，使用 map 函数，转化列表内每一个整形元素为字符串型。
# m 是可迭代类型，经过 list 转化后，看到列表 l。
m = map(lambda i: str(i), [111, 222, 3408])
print(m, type(m))
l = list(m)
print(l)
print(list(map(lambda x: x % 2 == 1, [1, 3, 2, 4, 1])))

# range(stop)；range(start, stop[,step])
# Python 提供两个内置的 range 函数，生成不可变序列：
print(range(11), type(range(11)))  # 只有一个参数，默认初始值为 0，步长为 1
print(range(0, 11))
print(range(0, 11, 1))  # 三个参数都提供，分别是开始、终止、步长值


# set([iterable])
# 返回一个集合对象，并允许创建后再增加、删除元素。
# 集合的一大优点，容器里不允许有重复元素，因此可对列表内的元素去重。
a = [1, 4, 2, 3, 1]
a1 = set(a)
print(a, a1)
# slice(stop)；slice(start, stop[, step])
# 返回一个由 range(start, stop, step) 所指定索引集的 slice 对象：
a = [1, 4, 2, 3, 1]
print(a[slice(0, 5, 2)])  # 等价于a[0:5:2]


# tuple([iterable])
# 创建一个不可修改的元组对象：
t = tuple(range(10))
print(t)
# type(object)；type(name, bases, dict)
# 这是两个查看对象的类型的函数。自定义类 Student，创建实例 xiaoming：
# type 函数是非常实用的，阅读他人代码时，若函数参数类型没有显示给出，就会用到 type 函数。


class StudentClass:
    pass


xiaoming = StudentClass()
print(type(xiaoming))

print(type((1, 2, 3)))


# zip(*iterables)
# 创建一个迭代器，聚合每个可迭代对象的元素。
# 参数前带 *，意味着是可变序列参数，可传入 1 个，2 个或多个参数。
# 传入 1 个参数：
for i in zip([1, 2]):
    print(i)
# 传入 2 个参数：
a = range(6)
b = list('abcde')
print(a, b)
l = [str(y)+str(x) for x, y in zip(a, b)]
print(l)


# 类对象及属性classmethod　　
# classmethod 修饰符对应的函数不需要实例化，不需要 self 参数。
# 第一个参数需要是表示自身类的 cls 参数，能调用类的属性、方法、实例等。
class Student():
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def instance_method(self):
        print("这是实例方法")

    @classmethod
    def __annotations__(cls):
        return "学生类"

    @classmethod
    def print_type_name(cls):
        print('这是类方法，类名为%s，注解为%s' % (cls.__name__, cls.__annotations__()))


Student().print_type_name()
Student().instance_method()

#delattr(object, name)　　
# 删除对象的属性，在不需要某个或某些属性时，这个方法就会很有用。
xiaoming = Student(1, "xiaoming")
print("xiaoming id is ", xiaoming.id)
delattr(xiaoming, 'id')
# hasaddttr(object, name)对象是否有属性name
print(hasattr(xiaoming, 'id'))
# print(xiaoming.id)#AttributeError: 'Student' object has no attribute 'id'

# dir([object])　　
# 不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时返回参数的属性、方法列表。
print(dir())
print(dir(xiaoming))

# getattr(object, name[, default])　　获取对象的属性：
print(getattr(xiaoming, 'name'))
#isinstance(object, classinfo)
# 判断 object 是否为类 classinfo 的实例，若是，返回 true。
print(isinstance(xiaoming, Student))
print(isinstance(xiaoming, StudentClass))

# issubclass(class, classinfo)
# 如果 class 是 classinfo 类的子类，返回 True：
print(issubclass(Student, object))
print(issubclass(object, Student))
# classinfo 取值也可能为元组，若 class 是元组内某个元素类型的子类，也会返回 True：
print(issubclass(int, (int, float)))


#property(fget=None, fset=None, fdel=None, doc=None)
# 返回 property 属性。不适用装饰器，定义类上的属性：

class StudentIns:
    def __init__(self):
        self._name = None

    def get_name(self):
        return self._name

    def set_name(self, val):
        self._name = val

    def del_name(self):
        del self._name
    # 显示调用 property 函数
    name = property(get_name, set_name, del_name, "name property")


xm = StudentIns()
xm.name = 'xm'
print(xm.name)
print(hasattr(xm, 'name'))
del xm.name
print(hasattr(xm, 'name'))


# 使用 Python 装饰器 @property，同样能实现对类上属性的定义 ，并且更简洁：

class StudentInfo:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @name.deleter
    def name(self):
        del self._name


xms = StudentInfo()
xms.name = 'xms'
print(xms.name)
print(hasattr(xms, 'name'))
del xms.name
print(hasattr(xms, 'name'))


# super([type[, object-or-type]])
# 返回一个代理对象，它会将方法调用委托给 type 的父类或兄弟类。
# 如下，子类的 add 方法，一部分直接调用父类 add，再有一部分个性的行为：打印结果。
class Parent():
    def __init__(self, x):
        self.v = x

    def add(self, x):
        return self.v+x


class Son(Parent):
    def add(self, y):
        r = super().add(y)
        print(r)


Son(1).add(2)

# callable(object)　
# 判断对象是否可被调用，能被调用的对象就是一个 callable 对象，
# 比如函数 str、int 等都是可被调用的。
print(callable(str), callable(int))
# 如下，xiaoming 实例不可被调用：
xms = Student()
print(callable(xms))
# 如果 xiaoming 能被调用,必须要重写 Student 类上 __call__ 方法：


class Stud():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __call__(self):
        print('I am callable')
        print(f"my name is {self.name}")


t = Stud(1, 'xiaoming')
t()
