#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:45:51 2018

@author: lux
"""
L = []
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    for e in aList:
        if type(e) == list:
            flatten(e)
        else:
            L.append(e)
    return L
        
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))