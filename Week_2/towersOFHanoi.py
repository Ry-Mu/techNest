#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 10:59:28 2017

@author: RyanMunguia
"""
#towersOfHanoi

count = 0
def printMove(fr, to):
    global count
    print('move from ' + str(fr) + ' to ' + str(to))
    count +=1

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(10, 'P1', 'P2', 'P3'))
print("Total Steps: ", count)