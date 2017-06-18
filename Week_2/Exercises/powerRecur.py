#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 12:41:54 2017

@author: RyanMunguia
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    
    returns: int or float, base^exp
    '''
    #Base case is when exp = 0
    
    if exp <= 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
    
    #Otherwise, exp must be > 0, so return
    #base * base^(exp-1). This is the recursive case.

print(recurPower(3,4))