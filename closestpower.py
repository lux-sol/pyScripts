#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 20:45:54 2018

@author: lux
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    i = 0
    while base ** i < int(num):
        i += 1
    if (base ** i) - int(num) >= int(num) - (base ** (i - 1)):
        return i - 1
    else:
        return i
    
print(closest_power(5, 375.0))
    