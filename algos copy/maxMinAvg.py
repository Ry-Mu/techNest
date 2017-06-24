#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:55:50 2017

@author: RyanMunguia
"""

#Given an array with multiple values, write a function that returns a new array
#that only contains the maximum, minimum, and average values of the original array. 
#(e.g. [1,5,10,-2] will return [10,-2,3.5])

def maxMinAvg(arr):
    sum = 0
    max = arr[0]
    min = arr[0]
    for i in arr:
        if i > max:
            max = i
        elif i < min:
            min = i
        sum += i
    av = sum/len(arr)
    newArr = [max,min,av]
    return newArr
    

print(maxMinAvg([1,5,10,-2]))
            
    

