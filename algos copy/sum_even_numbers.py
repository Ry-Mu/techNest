#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 19:02:13 2017

@author: RyanMunguia
"""

#Write a function that would get the sum of all the even numbers from 1 to 1000. 
#You may use a modulus operator for this exercise.

def sum_even_num():
    sum = 0
    for i in range(1,1001):
        if i % 2 == 0:
            sum += i
    return sum

print(sum_even_num())

