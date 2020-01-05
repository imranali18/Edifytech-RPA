# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:16:31 2019

@author: mushtu
"""

def list_fact(x):
    factorial=1
    for i in range(len(x)):
        for j in range(1,i+1):
            factorial=factorial*j
            i+=factorial
            factorial+=1
    print(x)
    
list_fact([2,3,4,5,8])
