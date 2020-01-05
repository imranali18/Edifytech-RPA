# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:03:21 2019

@author: mushtu
"""

def factorial(x):
    f=[]
    count=1
    a=1
    while a< len(x):
        for i in range(x[a]):
            count=count*(i+1)
        f.append(count)
        a+=1
    return f

factorial([2,3,4,5,8])
