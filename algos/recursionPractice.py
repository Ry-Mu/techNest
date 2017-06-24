#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 10:39:48 2017

@author: RyanMunguia
"""

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial(5))