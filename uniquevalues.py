#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:39:55 2018

@author: lux
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    testList = []
    L = []
    keys = []
    for e in aDict:
        testList.append(aDict[e])
        L.append(aDict[e])
    for i in testList: 
        if testList.count(i) > 1:
            L.remove(i)
    for e in aDict:
        if aDict[e] in L:
            keys.append(e)
            
    return keys

uniqueValues({1: 1, 2: 1, 3: 1, 4: 5})