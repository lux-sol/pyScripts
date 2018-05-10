#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 04:06:45 2018

@author: lux
"""

def simple_divide(item, denom):
    try: 
        return item / denom
    except ZeroDivisionError:
        print("Division by zero")

print(simple_divide(1,1))