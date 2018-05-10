#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 06:18:07 2018

@author: lux
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    midNum = int(len(aStr)/2)
    if len(aStr) <= 1 and aStr != char:
        return False
    elif char == aStr[midNum]:
        return True
    elif char < aStr[midNum]:
        return isIn(char, aStr[0:midNum])
    elif char > aStr[midNum]:
        return isIn(char, aStr[midNum + 1:])
    
print(isIn('d', 'ddoy'))