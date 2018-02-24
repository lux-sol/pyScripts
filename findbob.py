#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:27:47 2017

@author: lux
"""

s = "boboboobobbgyopobobftdobobbobbebobbb"
name = "bob"
i = 0
index = s.find(name)
for char in s:
    while index > -1:
        i = i+1
        index = s.find(name, index + 1)
print(i)
