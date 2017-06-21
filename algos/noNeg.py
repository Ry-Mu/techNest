#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:22:41 2017

@author: RyanMunguia
"""

"""
Given an array with multiple values, write a function that replaces any 
negative numbers within the array with the value of 0. 
When the program is done the array should contain no negative values. 
(e.g. [1,5,10,-2] will become [1,5,10,0])
"""

def noNeg(arr):
    array = []
    for i in arr:
        if i < 0:
            i = 0
        array.append(i)
    return array

print(noNeg([-11,5,10,-2,2,4,6,8,-3,-9,-99]))