#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:37:18 2017

@author: RyanMunguia
"""

#Write a function that will swap the first and last values of any given array. 
#The default minimum length of the array is 2. 
#(e.g. [1,5,10,-2] will become [-2,5,10,1]).

def swap(arr):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
    return arr

print(swap([1,5,10,-2]))