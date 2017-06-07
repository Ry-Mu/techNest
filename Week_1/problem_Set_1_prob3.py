#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:07:00 2017

@author: RyanMunguia
"""


s = 'azcbobobegghakl'

from itertools import count

maxSubstr = s[0:0]
for start in range(len(s)):
    for end in count(start + len(maxSubstr) + 1):
        substr = s[start:end]
        if len(substr) != (end - start):
            break
        if sorted(substr) == list(substr):
            maxSubstr = substr

print("Longest substring in alphabetical order is: " + str(maxSubstr))# Paste your code into this box 