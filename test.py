#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 04:41:55 2017

@author: lux
"""

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
print(foo(3))