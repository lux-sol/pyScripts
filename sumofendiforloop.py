#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 03:37:29 2017

@author: lux
"""

end = int(input("enter a number: "))
num = 0
for i in range(1, end + 1):
    num += i
print("The sum of the numbers from 0 to " + str(end) + " equals: " + str(num))