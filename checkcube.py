#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 04:32:51 2017

@author: lux
"""

cube = 8
for n in range(cube + 1):
    if n**3 == cube:
        print("The cube root of " + str(cube) + " is " + str(n))