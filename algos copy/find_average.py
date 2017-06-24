#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:36:21 2017

@author: RyanMunguia
"""

#Given an array with multiple values, write a function that returns the average
# of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)

def find_average(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum/len(arr)

print(find_average([3,3,3,9,7]))