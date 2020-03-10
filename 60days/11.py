'''
Day 11：Python 时间模块使用逻辑大盘点
Python 与时间处理相关模块有：time 模块和 datetime 模块。

time 模块， 提供 2 种时间表达方式：

假定一个零点基准，偏移长度换算为按秒的数值型
由 9 个整数组成的元组 struct_time 表示的时间
datetime 模块，常用类有 4 个：

date：日期类，包括属性年、月、日及相关方法
time：时间类，包括属性时、分、秒等及相关方法
datetime：日期时间，继承于 date，包括属性年、月、日、时、分、秒等及相关方法，其中年月日必须参数
timedelta：两个 datetime 值的差，比如相差几天（days）、几小时（hours）、几分（minutes）等。
除了以上 2 个时间模块外，calendar 模块还提供一些实用的功能，比如：
年、月的日历图
闰年判断
月有几天等等
'''
import time

seconds = time.time()
print(seconds)
local_time = time.localtime()
print(local_time)
str_time = time.asctime(local_time)
print(str_time)
format_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(format_time)
# time 类 strptime 方法，解析( parse) 输入的时间字符串为 struct_time 类型的时间。
# 注意：第二个参数的时间格式，要匹配上第一个参数的时间格式。
str_to_struct = time.strptime(format_time, '%Y-%m-%d %H:%M:%S')
print(str_to_struct)
'''
记住常用的时间格式：
    %Y  年
    %m  月 取值 [01,12]
    %d  天 取值 [01,31]
    %H  小时 取值 [00,23]
    %M  分钟 取值 [00,59]
    %S  秒 取值 [00,61]
'''
