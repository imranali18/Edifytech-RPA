# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:48:05 2019

@author: mushtu
"""

def list_fact(l):
    l2=[]
    for i in range(len(l)):
        x=1
        for j in range(1,l[i]+1):
            x=x*j
        l2.append(x)
    print(l2)
    
list_fact([2,3,4,5,8])
    