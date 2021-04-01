# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 01:12:06 2019

@author: winner
"""
# average
n = eval(input("How many numbers? "))
sum = 0.0
for i in range(n):
    x = eval(input("Enter a number>>"))
    sum += x;

print("\nThe average is:", sum / n)