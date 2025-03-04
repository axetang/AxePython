#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Repetition of patterns
"""

# end_pymotw_header
import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'
matches = re.findall(pattern, text)
print(type(matches), matches)
for match in re.findall(pattern, text):
    #print('Found {!r}'.format(match))
    print('Found {}'.format(match))
