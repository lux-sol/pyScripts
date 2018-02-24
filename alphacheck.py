#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:13:02 2017

@author: lux
"""
s = "abcdefabcdabcdefghiabcabc"
i = 0
alphaChars = s[i]
alphaSave = s[i]

while i + 1 < len(s):
    if s[i] <= s[i + 1]:
            alphaChars += s[i+1]
            i += 1
    else:
        i += 1
        alphaChars = s[i]
    if len(alphaChars) > len(alphaSave):
        alphaSave = alphaChars
print(alphaSave)