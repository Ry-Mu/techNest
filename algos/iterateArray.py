#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 19:56:15 2017

@author: RyanMunguia
"""

#Write a function that returns the sum of all the values within an array. 
#(e.g. [1,2,5] returns 8, [-5,2,5,12] returns 14)

def iterArr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print(iterArr([1,2,3,4,5,6,7,8,9,10]))
