#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:04:09 2017

@author: RyanMunguia
"""

#Given value of Y, write a function that takes an array and returns the number 
#of values that are greater than Y. 
#For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. 
#(There are two values in the array greater than 3, which are 5, 7).

def greaterY(arr, Y):
    count = 0
    for i in arr:
        if i > Y:
            count += 1
    return count

print(greaterY([0,1,2,3,4,5,6,7,8,9],7))
        
    