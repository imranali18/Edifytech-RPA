# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:42:43 2019

@author: mushtu
"""
import math
def list_fact(x):
    import math
    y=[]
    i=0
    while i<len(x):
        z=math.factorial(x[i])
        y.append(z)
        i+=1
    print(y)

list_fact([2,3,4,5,8])
