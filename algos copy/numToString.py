#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:42:45 2017

@author: RyanMunguia
"""

#Write a function that takes an array of numbers and replaces any negative values
#within the array with the string 'Dojo'. For example if array = [-1,-3,2], your
#function will return ['Dojo','Dojo',2].

def numToStr(arr):
    for i in arr:
        if i < 0:
            i = "CharlieFoo"
        return arr

print(numToStr([-1,-3,2]))