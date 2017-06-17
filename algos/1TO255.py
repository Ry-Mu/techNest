#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:00:47 2017

@author: RyanMunguia
"""

#Write a function that returns an array with all the numbers from 1 to 255. 
#You may use the push() function for this exercise.

def to255():
    array = []
    for i in range(0,256):
        array.append(i)
    return array

print(to255())