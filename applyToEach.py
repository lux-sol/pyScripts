#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:08:33 2018

@author: lux
"""
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    return len(aDict.values())
    
print(how_many(animals))

