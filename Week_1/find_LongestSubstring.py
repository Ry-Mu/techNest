#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 10:21:18 2017

@author: RyanMunguia
"""

s = "supercalifraaaaaaagilisticexpialidocious"
temp = []
temp.append(s[0])

ls = []
ls_len = 0

for i in range(0,len(s)-1):
    
    if s[i+1] >= s[i]:
        temp.append(s[i+1])
    else:
        if len(temp) > len(ls):
            ls = temp
            
        #reset temp
        temp = []
        temp.append(s[i + 1])

if len(temp) > len(ls):
    ls = temp
    
print("Longest substring is", ' '.join(ls))
print(ls)
print(temp)