#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 05:38:18 2018

@author: lux
"""

balance = 320000 
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
minimumFixedPayment = (lowerBound + upperBound) / 2
i = 0
check = False
checkBalance = balance


while check == False:
    while i < 12:
        monthlyUnpaidBalance = checkBalance - minimumFixedPayment
        updatedMonthlyBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        checkBalance = updatedMonthlyBalance
        i += 1
    if abs(round(checkBalance, 2)) <= 0.05:
        print(round(minimumFixedPayment, 2))
        check = True
    else:
        if checkBalance < 0:    
            upperBound = (lowerBound + upperBound) / 2
            minimumFixedPayment = (lowerBound + upperBound) / 2
        elif checkBalance > 0:
            lowerBound = (lowerBound + upperBound) / 2
            minimumFixedPayment = (lowerBound + upperBound) / 2
        checkBalance = balance
        i = 0