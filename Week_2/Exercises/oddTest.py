#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:14:41 2017

@author: RyanMunguia
"""

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return (x % 2 == 1)

print(odd(5))
print(odd(7))
print(odd(28))
print(odd(64))
print(odd(101))