
import re
from collections import defaultdict
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


file_name = '/Users/axe/AxeSpace/AxeGallery/20-Repo/AxeDev/AxePython/60days/bar.py'
ex = os.path.exists(file_name)
file_content = read_file(file_name)
print(file_content)

# 更常用的文件读写方法


def new_read_file(file_name):
    if os.path.exists(file_name) is False:
        raise FileNotFoundError('%s not exists!' % (file_name))
    with open(file_name, encoding="utf-8") as f:
        content = f.read()
    return content


file_name = '/Users/axe/AxeSpace/AxeGallery/20-Repo/AxeDev/AxePython/60days/bar.py'
print(new_read_file(file_name))

# from collections import defaultdict
# import re
rec = re.compile(r"\s+")
dd = defaultdict(int)
file_name = '/Users/axe/AxeSpace/AxeGallery/20-Repo/AxeDev/AxePython/60days/a.txt'
with open(file_name, 'r+') as f:
    for line in f:
        clean_line = line.strip()
        if clean_line:
            words = rec.split(clean_line)
            for word in words:
                dd[word] += 1


dd = sorted(dd.items(), key=lambda x: x[1], reverse=True)
print("-----print stat------")
print(dd)
print(type(dd))
print("-----print stat------")


def write_to_file(file_path, file_name):
    if os.path.exists(file_path) is False:
        os.mkdir(file_path)
    whole_path_file_name = os.path.join(file_path, file_name)
    print("whole_path_file_name: ", whole_path_file_name)
    to_write_content = '''
                        Hey, Python
                        I just love Python so much,
                        and want to get the whole python stack by this 60-days column
                        and believe!
                        '''
    with open(whole_path_file_name, mode='w') as f:
        f.write(to_write_content)
    print("---write done---")
    print("begin read")
    with open(whole_path_file_name) as f:
        content = f.read()
        print(content)
        if to_write_content == content:
            print("content is equal to reading and writing")
        else:
            print("Warning:No Equal!")


file_path = '/Users/axe/AxeSpace/AxeGallery/20-Repo/AxeDev/AxePython/60days/'
file_name = '/Users/axe/AxeSpace/AxeGallery/20-Repo/AxeDev/AxePython/60days/b.txt'
#file_name = 'b.txt'
write_to_file(file_path, file_name)


# 获取文件名
# 有时拿到一个文件名时，名字带有路径。这时，使用 os.path、split 方法实现路径和文件的分离。
file_ext = os.path.split(
    '/Users/axe/AxeSpace/AxeGallery/20-Repo/AxeDev/AxePython/60days/b.txt')
print(type(file_ext), file_ext)
ipath, ifile = file_ext
print(ipath, ifile)

# 获取后缀名
file_ext = os.path.splitext(
    '/Users/axe/AxeSpace/AxeGallery/20-Repo/AxeDev/AxePython/60days/b.txt')
print(type(file_ext), file_ext)
print(file_ext[0], file_ext[1])

# 获取后缀名的文件
print("获取后缀名的文件")


def find_file(work_dir, extension='py'):
    lst = []
    print("extension:", extension, "work_dir:", work_dir)
    for file_name in os.listdir(work_dir):
        # print(file_name)
        splits = os.path.splitext(file_name)
        ext = splits[1]
        if ext == '.'+extension:
            lst.append(file_name)
    return lst


r = find_file(".", "md")
print(r)
