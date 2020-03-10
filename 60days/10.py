
import time
import zipfile  # 导入 zipfile，这个是用来做；
from datetime import datetime
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

# 批量获取文件修改时间
# s.walk 生成文件树结构，os.path.getmtime 返回文件的最后一次修改时间：

print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def get_modify_time(indir):
    for root, _, files in os.walk(indir):  # 循环目录和子目录
        print(root, type(root))
        for file in files:
            whole_file_name = os.path.join(root, file)
            # 1581164725.991523，这种时间格式太不人性化
            modify_time = os.path.getmtime(whole_file_name)
            # 转化为人性化的时间显示格式：2020-02-08 20:25:25.991523
            nice_show_time = datetime.fromtimestamp(modify_time)
            print('文件 %s/%s 最后一次修改时间：%s' % (root, file, nice_show_time))


get_modify_time('./files')


# 批量压缩文件
# 首先导入 zipfile，压缩和解压的 Python 模块。
# import zipfile
#import os
#import time


def batch_zip(start_dir):
    start_dir = start_dir  # 要压缩的文件夹路径
    file_news = start_dir + '.zip'  # 压缩后文件夹的名字

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        # 这一句很重要，不 replace 的话，就从根目录开始复制
        f_path = dir_path.replace(start_dir, '')
        f_path = f_path and f_path + os.sep  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    return file_news


"""未完成
批量压缩文件

首先导入 zipfile，压缩和解压的 Python 模块。

import zipfile  # 导入 zipfile，这个是用来做；
import os
import time


def batch_zip(start_dir):
    start_dir = start_dir  # 要压缩的文件夹路径
    file_news = start_dir + '.zip'  # 压缩后文件夹的名字

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        # 这一句很重要，不 replace 的话，就从根目录开始复制
        f_path = dir_path.replace(start_dir, '')
        f_path = f_path and f_path + os.sep  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    return file_news
调用 batch_zip，压缩 ziptest 文件夹。

batch_zip('./data/ziptest')
32 位文件加密

hashlib 模块支持多种文件的加密策略。本案例使用 MD5 加密策略：

import hashlib
# 对字符串 s 实现 32 位加密


def hash_cry32(s):
    m = hashlib.md5()
    m.update((str(s).encode('utf-8')))
    return m.hexdigest()


print(hash_cry32(1))  # c4ca4238a0b923820dcc509a6f75849b
print(hash_cry32('hello'))  # 5d41402abc4b2a76b9719d911017c592
定制文件不同行

比较两个文件在哪些行内容不同，返回这些行的编号，行号编号从 1 开始。

定义统计文件行数的函数：

# 统计文件个数
    def statLineCnt(statfile):
        print('文件名：'+statfile)
        cnt = 0
        with open(statfile, encoding='utf-8') as f:
            while f.readline():
                cnt += 1
            return cnt
统计文件不同之处的子函数：

# more表示含有更多行数的文件
        def diff(more, cnt, less):
            difflist = []
            with open(less, encoding='utf-8') as l:
                with open(more, encoding='utf-8') as m:
                    lines = l.readlines()
                    for i, line in enumerate(lines):
                        if line.strip() != m.readline().strip():
                            difflist.append(i)
            if cnt - i > 1:
                difflist.extend(range(i + 1, cnt))
            return [no+1 for no in difflist]
主函数：

# 返回的结果行号从 1 开始
# list 表示 fileA 和 fileB 不同的行的编号

def file_diff_line_nos(fileA, fileB):
    try:
        cntA = statLineCnt(fileA)
        cntB = statLineCnt(fileB)
        if cntA > cntB:
            return diff(fileA, cntA, fileB)
        return diff(fileB, cntB, fileA)

    except Exception as e:
        print(e)
比较两个文件 A 和 B，拿相对较短的文件去比较，过滤行后的换行符 \n 和空格。

暂未考虑某个文件最后可能有的多行空行等特殊情况。

使用 file_diff_line_nos 函数：

if __name__ == '__main__':
    import os
    print(os.getcwd())

    '''
例子：
fileA = "'hello world!!!!''\
            'nice to meet you'\
            'yes'\
            'no1'\
            'jack'"
fileB = "'hello world!!!!''\
            'nice to meet you'\
            'yes' "
'''
    diff = file_diff_line_nos('./testdir/a.txt', './testdir/b.txt')
    print(diff)  # [4, 5]
实际上 Python 中有对应模块 difflib，提供更多其他格式文件更详细的比较，大家可参考：

https://docs.python.org/3/library/difflib.html?highlight=difflib#module-difflib

"""
