#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 00:40:41 2018

@author: lux
"""
x = 10
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    i = 0
    k = len(L) - 1
    for e in L:
        i += (e * (x**(k)))
        k -= 1
    print(i)
    return i
        
    
    
    
general_poly([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])