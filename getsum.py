#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 04:29:39 2017

@author: lux
"""

def get_sum(a,b):
    if a == b:
        print(a)
    else:
        diff = abs(a-b)
        i = 0
        if a < b:
            minNum = a
        else:
            minNum = b
        c = minNum
        while i < diff:
            i += 1
            c = c + (minNum + i)
    print(c)
    
get_sum(-1,2)