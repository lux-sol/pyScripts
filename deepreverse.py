#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:08:58 2018

@author: lux
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    for e in L:
        e.reverse()
    L = L[::-1]
    print(L)
    
deep_reverse([[1], [1, 2, 3]])