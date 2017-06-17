#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 19:02:13 2017

@author: RyanMunguia
"""


def sum_even_num():
    sum = 0
    for i in range(1,1001):
        if i % 2 == 0:
            sum += i
    return sum

print(sum_even_num())

