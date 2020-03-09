
'''
Day 10：Python 文件操作 11 个案例总结
Python 文件 IO 操作：

涉及文件读写操作
获取文件后缀名
批量修改后缀名
获取文件修改时间
压缩文件
加密文件等常用操作
'''

# 文件读操作
# 文件读、写操作比较常见。读取文件，要先判断文件是否存在。
# 若文件存在，再读取；不存在，抛出文件不存在异常。

# import os
import os


def read_file(file_name):
    if os.path.exists(file_name) is False:
        raise FileNotFoundError('%s not exists!' % (file_name,))

    f = open(file_name, encoding="utf-8")
    content = f.read()
    f.close()
    return content


file_content = read_file('./bar.py')
print(file_content)

# 更常用的文件读写方法


def new_read_file(file_name):
    if os.path.exists(file_name) is False:
        raise FileNotFoundError('%s not exists!' % (file_name))
    with open(file_name, encoding="utf-8") as f:
        content = f.read()
    return content


print(new_read_file("./bar.py"))
