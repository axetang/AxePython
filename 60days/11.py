from datetime import date
import calendar
from datetime import date, datetime, time, timedelta
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
# datetime 模块
# 从 datetime 模块中，依次导入类：date、datetime、time、timedelta。
#from datetime import date, datetime, time, timedelta
tod = date.today()
print(tod, type(tod))
str_date = date.strftime(tod, '%Y-%m-%d')
print(str_date)

# 字符日期转日期
# date 类里没有 strptime 方法，它的子类 datetime 才有解析字符串日期的方法 strptime。
str_to_date = datetime.strptime('2020-03-11', '%Y-%m-%d')
print(str_to_date, type(str_to_date))

right = datetime.now()
print(right)

str_time = datetime.strftime(right, '%Y-%m-%d %H:%M:%S')
print(str_time)

str_to_time = datetime.strptime('2020-02-22 15:12:33', '%Y-%m-%d %H:%M:%S')
print(str_to_time)


# timedelta
# 求两个 datetime 类型值的差，返回差几天：days，差几小时：hours 等。
# 相减的两个时间，不能一个为 date 类型，一个为 datetime 类型，尽管两个类型是父子关系。
def get_days_girlfriend(birthday: str)->int:
    import re
    splits = re.split(r'[-.\s+/]', birthday)
    print(splits)
    splits = [s for s in splits if s]  # 去掉空格字符
    print(splits)
    if len(splits) < 3:
        raise ValueError('输入格式不正确，至少包括年月日')
    splits = splits[:3]  # 只截取年月日
    birthday = datetime.strptime('-'.join(splits), '%Y-%m-%d')
    tod = date.today()
    delta = birthday.date() - tod
    return delta.days


delta = get_days_girlfriend('2020-05-20')
print(delta)
delta = get_days_girlfriend('2020/5/20')
print(delta)
delta = get_days_girlfriend('2021 1    9')
print(delta)
delta = get_days_girlfriend('2020/5/20 10:00')
print(delta)


# 绘制年的日历图
#import calendar
#from datetime import date
mydate = date.today()
print(type(mydate), type(mydate.year))
year_calendar_str = calendar.calendar(mydate.year)
print(f"{mydate.year}年的日历图：\n{year_calendar_str}\n")


#import calendar
#from datetime import date

mydate = date.today()
is_leap = calendar.isleap(mydate.year)
print_leap_str = "%s年是闰年" if is_leap else "%s年不是闰年\n"
print(print_leap_str % mydate.year)


# 判断月有几天
#import calendar
#from datetime import date
mydate = date.today()
weekday, days = calendar.monthrange(mydate.year, mydate.month)
print(f'{mydate.year}年-{mydate.month}月的第一天是那一周的第{weekday}天\n')
print(f'{mydate.year}年-{mydate.month}月共有{days}天\n')

# 月的第一天
# from datetime import date
mydate = date.today()
month_first_day = date(mydate.year, mydate.month, 1)
print(f"当月第一天:{month_first_day}\n")
# 月的最后一天
mydate = datetime.strptime('2020-02-21', '%Y-%m-%d')
_, days = calendar.monthrange(mydate.year, mydate.month)
month_last_day = date(mydate.year, mydate.month, days)
print(f"当月最后一天:{month_last_day}\n")
