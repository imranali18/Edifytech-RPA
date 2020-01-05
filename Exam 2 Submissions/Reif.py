# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:58:49 2019

@author: mushtu
"""

def list_fact(numbers):
    j=[0]
    for numbers in numbers:
        i=j
        while j<=len(numbers):
            numbers[j]*i
            i-=1
            j+=1
    