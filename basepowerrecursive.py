#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 04:43:48 2018

@author: lux
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    num = 0
    if num == exp:
        return 1
    else:
      return base * recurPower(base, exp-1)
print(recurPower(4,5))