#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:06:57 2017

@author: RyanMunguia
"""

#Write a function that would return an array of all the odd numbers between 1 to 50.
#(ex. [1,3,5, .... , 47,49]). Hint: Use 'append' method.

def oddNumbers():
    arr = []
    for i in range(1,51,2):
        arr.append(i)
    return arr

print(oddNumbers())