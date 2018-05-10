#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 03:32:46 2018

@author: lux
"""

def payDebt (balance, annualInterestRate, monthlyPaymentRate, i = 1):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    if i < 12:
        i += 1
        payDebt(updatedBalance, annualInterestRate, monthlyPaymentRate, i)
    else:
        print(round(updatedBalance, 2))

payDebt(484, 0.2, 0.04)