#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 19:26:34 2017

@author: RyanMunguia
"""

#Write a function that returns the sum of all the odd numbers from 1 to 5000. 
#(e.g. 1+3+5+...+4997+4999)

def sum_odd_5000():
    sum = 0
    for i in range(1,5001):
        if i % 2 == 1:
            sum += i
    return sum

print(sum_odd_5000())