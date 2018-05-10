#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 01:47:31 2018

@author: lux
"""

animals = {'a': ['aardvark', 'apple', 'aligator', 'alexa', 'aaron'],'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    key = []
    i = 0
    for elmnt in aDict:
        if len(aDict[elmnt]) > i:
            i = len(aDict[elmnt])
            key = elmnt
    return key

print(biggest(animals))