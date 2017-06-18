#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 12:37:10 2017

@author: RyanMunguia
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

print(iterPower(3,3))