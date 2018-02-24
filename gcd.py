#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 05:15:47 2018

@author: lux
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if (a <= b):
        gcd = a
    else:
        gcd = b
    for i in range (1, gcd + 1):
        if (gcd == 1):
            return(gcd)
        elif (a%gcd == 0 and b % gcd == 0):
            return(gcd)
        else:
            gcd = gcd - 1
gcdIter(65,117)