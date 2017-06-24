#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:10:44 2017

@author: RyanMunguia
"""

#Given an array with multiple values, write a function that replaces each value
#in the array with the product of the original value squared by itself. 
#(e.g. [1,5,10,-2] will become [1,25,100,4])

def squareVal(arr):
    array = []
    for i in arr:
        array.append(i**2)
    return array

print(squareVal([1,5,10,-2,2,4,6,8,3,6,9]))