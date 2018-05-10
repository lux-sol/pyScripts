#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 04:39:26 2018

@author: lux
"""

balance = 4773
annualInterestRate = 0.2

minimumFixedPayment = 10
i = 0
check = False
checkBalance = balance
while check == False:
    while i < 12:
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = checkBalance - minimumFixedPayment
        updatedMonthlyBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        checkBalance = updatedMonthlyBalance
        i += 1
    if checkBalance <= 0:
        print(minimumFixedPayment)
        check = True
    else:
        minimumFixedPayment += 10
        checkBalance = balance
        i = 0

 

