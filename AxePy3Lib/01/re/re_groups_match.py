#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Looking at groups on a match object
"""

# end_pymotw_header
import re

text = 'This is some text -- with punctuation.'

print(text)
print()

patterns = [
    (r'^(\w+)', 'word at start of string'),
    (r'(\w+)\S*$', 'word at end, with optional punctuation'),
    (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
    (r'(\w+t)\b', 'word ending with t'),
]

for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}' ({})\n".format(pattern, desc))
    print('  ', match.groups())
    print()

print("my test")
text = 'This is some texth -- wxith punctuation.'
pattern = r'(\w+x)(\w+h)'
regex = re.compile(pattern)
# 记住：search只能在字符串中搜索一次，找到一个匹配结果
match = regex.search(text)
print('  ', match)
print('  ', type(match.groups()))
print('  ', match.groups())

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print(match.groups())
    print(match.group(0), match.group(1), match.group(2))
