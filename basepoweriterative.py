#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 04:11:23 2018

@author: lux
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    num = 1
    for i in range (1, exp + 1):
          num = num*base
    return num
print(iterPower(-3.71, 6))