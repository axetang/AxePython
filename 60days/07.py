d = {'a': 1, 'b': 20, 'c': 3}
print(len(d))

# max(iterable,*[,key,default])，返回最大值
print(max(3, 4, 5, 1, 3))
print(max((), default=0))
print(max(d), max(d.keys()))
print(max(d.values()))

a = [{'name': 'axe', 'age': 40, 'gender': 'male'},
     {'name': 'lucas', 'age': 10, 'gender': 'male'},
     {'name': 'wyy', 'age': 30, 'gender': 'female'}]

da = max(a, key=lambda x: x['age'])
print(da, type(da))

# max、min 函数都有一个参数 key，它们也被称为 key 函数，
# key函数一般结合更紧凑的lambda函数。max有一个default参数：
# 当传入的列表为空时，若参数 default 被赋值，则返回 default；
# 否则，会抛空序列的异常（empty sequence）


def max_lenth(*lst):
    # 如果已知多个列表，找出列表更长的，使用 max 方法：
    return max(*lst, key=lambda v: len(v))


print(max_lenth([1, 2, 3], [2, 3, 4], [4, 5, 6, 7]))
print(max([], default=0))
# print(max([]))  # ValueError: max() arg is an empty sequence


#
# pow(x, y, z=None, /)
# x 为底的 y 次幂，如果 z 给出，取余：
print('pow:', pow(3, 2, 4))
# round(number[, ndigits])
# 四舍五入，ndigits 代表小数点后保留几位：
print("round:", round(10.02222, 3))
# sum(iterable, / , start=0)
# 求和：
a = [1, 3, 5, 7, 9]
print('sum:', sum(a))
print(sum(a, 10))
# abs(x, / )
# 求绝对值或复数的模：
print("abs:", abs(-100))
#divmod(a, b)
# 分别取商和余数：
print('divmod:', divmod(10, 3))
# complex([real[, imag]])
# 创建一个复数：
print("complex:", complex(10, 20))


class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id='+self.id+" "+"name="+self.name


# hash(object)　　返回对象的哈希值：
# id(object)　　返回对象的内存地址
xiaoming = Student('001', 'xiaoming')
print(hash(xiaoming), type(hash(xiaoming)))
print(id(xiaoming), type(id(xiaoming)))

# all(iterable)
# 接受一个迭代器，如果迭代器的所有元素都为真，返回 True，否则返回 False：
print(all((1, 2, 3, 4)))
print(all([10, 0, 5, 8]))
# any(iterable)　
# 接受一个迭代器，如果迭代器里有一个元素为真，返回 True，否则返回 False：
print(any([0, 1, 2, 3]))
print(any([1, 2, 3]))
print(any([0, 0, 0, []]))


# ascii(object)　　
# 调用对象__repr__() 方法，获得该方法的返回值。
print(xiaoming)
print(ascii(xiaoming))


# bin(x)将十进制转换为二进制：
# oct(x)将十进制转换为八进制：
# hex(x)将十进制转换为十六进制：

print(bin(-1023))
print(bin(1023))
print(oct(9))
print(oct(-9))
print(hex(15))
print(hex(-15))
