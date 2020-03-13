#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Show all matches for a list of patterns.
"""

# end_pymotw_header
import re


def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        # 记住，regex.search()函数只能从字符串中搜索到第一次匹配的结果，不能搜出全部匹配结果
        # 要使用re.finditer来构造迭代器实现全部match的搜索和处理
        # pattern中用小括号对来封装正则表达式的子分组，按照左小括号出现顺序来确定match.group()的参数
        # 可以使用match.groups()和match.group(x)来获取子表达式的匹配结果
        # regex= re.compile(pattern)
        # match = regex.search(text)
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            prefix = '.'*s
            print("  {}'{}'".format(prefix, substr))
            # print(match.groups())
            # print(match.group(0),match.group(1),match.group(2))
        print()
    return


if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa', [('ab', "'a' followed by 'b'"),
                                      ('ba', "'b' followed by 'a'")])
    print("-----------------------")
    text = 'abbaaabbbbaaaaa'
    # patts = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    # patts = [('a', 'b'), ('c', 'd'), ('e', 'f')]
    # for pat, desc in patts:
    patts = {'ab': '12', 'ba': '21', 'aba': '121'}
    for pat, desc in patts.items():
        print("pat is {0!r}, desc is {1!r}".format(pat, desc))
        for match in re.finditer(pat, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            print(s, e, substr)
