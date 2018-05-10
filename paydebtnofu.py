#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 04:24:17 2018

@author: lux
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
i = 0
while i < 12:
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    balance = updatedBalance
    i += 1
print(round(updatedBalance, 2))