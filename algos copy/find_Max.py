#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:09:19 2017

@author: RyanMunguia
"""

#Given an array with multiple values, write a function that returns the maximum
#number in the array. (e.g. for [-3,3,5,7] max is 7)

def find_max(arr):
    max = 0
    for i in arr:
        if max < i:
            max = i
    return max

print(find_max([2,4,5,64,2,3,7,33,2]))