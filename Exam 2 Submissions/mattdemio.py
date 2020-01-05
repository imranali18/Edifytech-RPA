# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:18:58 2019

@author: mushtu
"""

def list_fact(x):
    l=[]
    for y in x:
        factorial = 1
        for z in range(y+1):
            factorial=factorial*z
        else:
            l.append(factorial)
    return l

list_fact([2,3,4,5,8])
