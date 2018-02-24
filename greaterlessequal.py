#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 02:40:56 2017

@author: lux
"""
varA = "five"
varB = 4

if type(varA) == str:
    print("string involved")
elif type(varB) == str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")