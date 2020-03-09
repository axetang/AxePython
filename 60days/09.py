import re
'''
Day 9：Python 字符串和正则介绍总结
字符串无所不在，字符串的处理也是最常见的操作,主要包括：
    基本的字符串操作
    高级字符串操作之正则部分
'''
# 基本操作
s = 'Python'
rs = ''.join(reversed(s))
print(rs)

# 字符串切片操作
# 生成 1 到 15 的序列，并在满足条件的索引处，替换为 java 或 python。
java, python = "Java", "Python"
jl, pl = len(java), len(python)
print('str(java[jl]):', str(java[jl:]))
print([str(java[i % 3*jl:] + python[i % 5*pl:] or i) for i in range(1, 10)])

# join 串联字符串:用下划线 _ 连接字符串 mystr：
mystr = ["i", 'love', 'python']
res = "_".join(mystr)
print(res)

# 分割字符串
# 根据指定字符或字符串，分割一个字符串时，使用方法 split。
# join 和 split 可看做一对互逆操作：
print(res.split("_"))

# 字符串替换，使用 replace 方法。注意：只替换首次发现的
s = 'i love python'.replace('o', 'O')
s = 'i love python'.replace('ov', 'OV')
print(s)

# 子串判断:判断 a 串是否为 b 串的子串。
# 方法 1，使用 in：
a = "our"
b = "flourish"
r = True if a in b else False
print(r)
# 方法 2，使用方法 find，返回字符串 b 中匹配子串 a 的最小索引：
print(b.find(a))


# 去空格
# 清洗字符串时，位于字符串开始和结尾的空格，有时需要去掉，strip 方法能实现。
# 如下字符串，使用 strip，清理字符串开头和结尾的空格和制表符。
a = "  \tI love Python    \b\n"
print(a)
print(a.strip())

# 字符串的字节长度
# encode 方法对字符串编码后：


def str_byte_len(mystr):
    mystr_bytes = mystr.encode('utf-8')
    return(len(mystr_bytes))


print(str_byte_len('I love Python'))
print(str_byte_len('我爱Python'))
print(str_byte_len('我爱'))


'''
正则表达式
字符串封装的方法，处理一般的字符串操作，还能应付。但是，稍微复杂点的字符串处理任务,
需要靠正则表达式，简洁且强大。
首先，导入所需要的模块 re：
    import re
认识常用的元字符：
. 匹配除 "\n" 和 "\r" 之外的任何单个字符。
^ 匹配字符串开始位置
$ 匹配字符串中结束的位置
* 前面的原子重复 0 次、1 次、多次
? 前面的原子重复 0 次或者 1 次
+ 前面的原子重复 1 次或多次
{n} 前面的原子出现了 n 次
{n,} 前面的原子至少出现 n 次
{n,m} 前面的原子出现次数介于 n-m 之间
( ) 分组，输出需要的部分
再认识常用的通用字符：
\s 匹配空白字符
\w 匹配任意字母/数字/下划线
\W 和小写 w 相反，匹配任意字母/数字/下划线以外的字符
\d 匹配十进制数字
\D 匹配除了十进制数以外的值
[0-9] 匹配一个 0~9 之间的数字
[a-z] 匹配小写英文字母
[A-Z] 匹配大写英文字母
正则表达式，常会涉及到以上这些元字符或通用字符，
'''

# import re
s = 'i love python very much'
pat = 'python'
r = re.search(pat, s)
print(type(r), r)
print(r.span())


# match 与 search 不同
# 正则模块中，match、search 方法匹配字符串不同
# match 在原字符串的开始位置匹配
# search 在字符串的任意位置匹配
s = 'flourish'
recom = re.compile('our')
print(recom.match(s))
print(recom.search(s))
print(recom.search('ourselves'))


# finditer 匹配迭代器
print("finditer:")
# 使用正则模块，finditer 方法，返回所有子串匹配位置的迭代器。
# 通过返回的对象 re.Match，使用它的方法 span 找出匹配位置
s = '山东省潍坊市青州第1中学高三1班'
pat = '1'
r = re.finditer(pat, s)
for i in r:
    print(i)


# findall 所有匹配
# 正则模块，findall 方法能查找出子串的所有匹配。
# 原字符串 s：
s = '一共2行代码运行时间13.59s'
# 目标查找出所有所有数字：通用字符 \d 匹配一位数字 [0-9]，
# + 表示匹配数字前面的一个字符 1 次或多次。
pat = r'\d+'
r = re.findall(pat, s)
print(r)

# 匹配浮点数和整数
#   ? 表示前一个字符匹配 0 或 1 次
#   .? 表示匹配小数点（.）0 次或 1 次。
pat = r'\d+\.?\d+'
r = re.findall(pat, s)
print(r)
pat = r'\d+\.?\d*'
r = re.findall(pat, s)
print(r)


# 案例：写出匹配所有正整数的正则表达式。
# 如果这样写：^\d*$，会匹配到 0，所以不准确。
# 如果这样写：^[1-9]*，会匹配 1. 串中 1，不是完全匹配，体会 $ 的作用。
# 正确写法：^[1-9]\d*$，
s = [-16, 1.5, 11.43, 10, 5]
pat = r'^[1-9]\d*$'
print([i for i in s if re.match(pat, str(i))])


# re.I 忽略大小写
# re.I 是方法的可选参数，表示忽略大小写。
# 如下，找出字符串中所有字符 t 或 T 的位置，不区分大小写。
s = "That"
pat = r't'
r = re.finditer(pat, s, re.I)
for i in r:
    print(i.span())


# split 分割单词
'''
正则模块中 split 函数强大，能够处理复杂的字符串分割任务。
如果一个规则简单的字符串，直接使用字符串，split 函数。
如下字符串，根据分割符 \t 分割：
In [91]: s = 'id\tname\taddress'
In [92]: s.split('\t')
Out[92]: ['id', 'name', 'address']
但是，对于分隔符复杂的字符串，split 函数就无能为力。
如下字符串，可能的分隔符有 ,、;、\t、|。
'''
s = 'This,,,   module ; \t   provides|| regular ; '
words = re.split(r'[,\s;|]+', s)
print(words)


# sub 替换匹配串:正则模块，sub 方法，替换匹配到的子串：
content = "hello 12345, hello 456321"
pat = re.compile(r'\d+')  # 要替换的部分
m = pat.sub("666", content)
print(m)


# compile 预编译
# 如果要用同一匹配模式，做很多次匹配，可以使用 compile 预先编译串。
# 案例：从一系列字符串中，挑选出所有正浮点数。
# 正则表达式为：^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$，
# 字符 a|b 表示 a 串匹配失败后，才执行 b 串

# 首先，生成预编译对象 rec：
s = [-16, 'good', 1.5, 0.2, -0.1, '11.43', 10, '5e10']
rec = re.compile(r'^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$')
# 下面直接使用 rec，匹配列表中的每个元素，不用每次都预编译正则表达式，效率更高。
m = [i for i in s if rec.match(str(i))]
print(m)


# 贪心捕获和费贪心捕获:未完成
"""
贪心捕获

正则模块中，根据某个模式串，匹配到结果。

待爬取网页的部分内容如下所示，现在想要提取 <div> 标签中的内容。

In [125]: content = '''
...: < h > ddedadsad < /h >
...: < div > graph < /div >
...: < div > math < /div > '''
如果正则匹配串写做 <div>.*</div>：

In [118]: result = re.findall(r'<div>.*</div>',content)

In [119]: result
Out[119]: ['<div>graph</div>bb<div>math</div>']
返回的结果：

'<div>graph</div>bb<div>math</div>' 
如果我们不想保留字符串最开始的 <div> 和结尾的 </div>，那么，就需要使用一对 () 去捕获。

正则匹配串修改为：<div>(.*)</div>，只添加一对括号。

In [120]: result = re.findall(r'<div>(.*)</div>',content)

In [121]: result
Out[121]: ['graph</div>bb<div>math']
看到结果中已经没有开始的 <div>，结尾的 </div> 仅使用一对括号，便成功捕获到我们想要的部分。
(.*) 表示捕获任意多个字符，尽可能多地匹配字符，也被称为贪心捕获
(.*) 的正则分解图如下所示，. 表示匹配除换行符外的任意字符。
image-20200220213002588

非贪心捕获

观察上面返回的结果 ['graph</div>bb<div>math']，如果只想要得到两个 <div></div> 间的内容，该怎么写正则表达式？

相比 (.*)，仅多添加一个 ?，匹配串为 (.*?)。

In [125]: content = '''
...: < h > ddedadsad < /h >
...: < div > graph < /div >
...: < div > math < /div > '''

In [126]: result = re.findall(r'<div>(.*?)</div>',content)

In [127]: result
Out[127]: ['graph', 'math']
终于得到 2 个 <div> 对间的内容。

这种匹配模式串 (.*?)，被称为非贪心捕获。正则图中，红色虚线表示非贪心匹配。
"""
