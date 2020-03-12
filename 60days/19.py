from math import ceil
'''
直观理解 yield
要想通俗理解 yield，可结合函数的返回值关键字 return，yield 是一种特殊的 return。
说是特殊的 return，是因为执行遇到 yield 时，立即返回，这是与 return 的相似之处。
不同之处在于：下次进入函数时直接到 yield 的下一个语句，而 return 后再进入函数，
还是从函数体的第一行代码开始执行。带 yield 的函数是生成器，通常与 next 函数结合用。
下次进入函数，意思是使用 next 函数进入到函数体内。
'''


def f():
    print("enter f()...")
    yield 4
    print("i am next sentence of yield.")


g = f()
active = True
i = 0
while(active):
    i += 1
    try:
        next(g)
    except StopIteration:
        print(f"%d times, Iteration Stop" % i)
        break

# yield 与生成器
# 函数带有 yield，就是一个生成器，英文 generator，它的重要优点之一节省内存。


def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


for i in myrange(10):
    print(i)


# send 函数
# 带 yield 的生成器对象里还封装了一个 send 方法。
# 下例暂时send用法，send函数赋值给yield左侧的result变量，然后继续执行yield的下一句
def f():
    print('enter f...')
    while True:
        result = yield 4
        if result:
            print('send me a value is:%d' % (result,))
            return
        else:
            print('no send', result)


g = f()
print(next(g))
print('ready to send')
print(g.send(None))
print(g.send(''))
print(g.send(False))
# print(g.send(10))


# 1. 完全展开 list
# 下面的函数 deep_flatten 定义中使用了 yield 关键字，实现嵌套 list 的完全展开。

def deep_flatten(lst):
    for i in lst:
        if type(i) == list:
            yield from deep_flatten(i)
        else:
            yield i


gen = deep_flatten([1, ['s', ['a', 'b'], 3], 4, 5])
print(gen)

for i in gen:
    print(i)


# 2. 列表分组
#from math import ceil


def divide_iter(lst, n):
    if n <= 0:
        yield lst
        return
    i, div = 0, ceil(len(lst) / n)
    while i < n:
        yield lst[i * div: (i + 1) * div]
        i += 1


print(list(divide_iter([1, 2, 3, 4, 5], 0)))  # [[1, 2, 3, 4, 5]]
print(list(divide_iter([1, 2, 3, 4, 5], 2)))  # [[1, 2, 3], [4, 5]]


'''
nonlocal 关键字
关键词 nonlocal 常用于函数嵌套中，声明变量为非局部变量。
'''


def ff():
    i = 0

    def auto_increase():
        nonlocal i  # 使用 nonlocal 告诉编译器，i 不是局部变量
        if i >= 10:
            i = 0
        i += 1
    ret = []
    for _ in range(28):
        auto_increase()
        ret.append(i)
    print(ret)


ff()
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4,5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

#######################
#global 关键字
# 先回答为什么要有 global。
# 一个变量被多个函数引用，想让全局变量被所有函数共享。
# 有的伙伴可能会想这还不简单，这样写：

i = 5


def f():
    print(i)


def g():
    print(i)
    pass


f()
g()
# f 和 g 两个函数都能共享变量 i，程序没有报错，所以，至此依然没有真正解释global 存在的价值。
# 但是，如果某个函数要修改 i，实现递增，这样：


def h():
    i += 1


h()
# 此时执行程序，就会出错，抛出异常 UnboundLocalError，原来编译器在解释 i += 1 时，
# 会解析 i 为函数 h() 内的局部变量。很显然，在此函数内，解释器找不到对变量 i 的定义，所以报错。

# global 在此种场景下，会大显身手。

# 在函数 h 内，显示地告诉解释器 i 为全局变量，然后，解释器会在函数外面寻找 i 的定义，
# 执行完 i += 1 后，i 还为全局变量，值加 1：

i = 0


def hh():
    global i
    i += 1


h()
print(i)
