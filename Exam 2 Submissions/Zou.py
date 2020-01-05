# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:09:08 2019

@author: mushtu
"""

def list_fact(a):
    fact=1
    for i in range(len(a)):
        fact=fact*(i+1)
    print(fact)
    
list_fact([2,3,4,5,8])
