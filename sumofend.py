#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 02:56:58 2017

@author: lux
"""
end = int(input("enter a number: "))
num = 0
x = 0
while x < end:
    x += 1
    num += x
print("The sum of the numbers from 0 to " + str(end) + " equals: " + str(num))