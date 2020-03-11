#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
import string

values = {'var': 'foo', 'const': 100}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

t = string.Template("""
Variable        : $const
Escape          : $$
Variable in text: ${const}iable
""")

print('TEMPLATE:', t.substitute(values))
print("-----------------------------------")

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : %(const)s
Escape          : %%
Variable in text: %(const)siable
"""

print('INTERPOLATION:', s % values)
print("-----------------------------------")

# 在字符串中使用大括号{}需要用大括号进行转义
s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))
print('Format:', s.format(var='fool', const=100))

s = """
Variable        : {const}
Escape          : {{}}
Variable in text: {const}iable
"""

print('FORMAT:', s.format(**values))
print('Format:', s.format(var='foo', const=100))

s = """
{{}} is {var}
"""
print(s)
print(s.format(**values))
