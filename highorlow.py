#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 04:03:01 2017

@author: lux
"""
guessMax = 100
guessMin = 0
guess = 50
correct = False
print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(int(guess)) + "?")
check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while (correct == False):
    if(check == "h"):
        guessMax = guess
        guess = int(guessMin + ((guessMax - guessMin) / 2))
        print("Is your secret number " + str(int(guess)) + "?")
        check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif(check == "l"):
        guessMin = guess
        guess = int(guessMin + ((guessMax - guessMin) / 2))
        print("Is your secret number " + str(int(guess)) + "?")
        check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif(check == "c"):
        correct = True
        print("Game over. Your secret number was: " + str(int(guess)))
    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(int(guess)) + "?")
        check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
   