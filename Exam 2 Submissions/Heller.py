# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:33:27 2019

@author: mushtu
"""

def list_fact(a):
    l1=[]
    i=0
    j=0
    while i in range(len(a)):
        while j in range(a[i]):
            x=j*(j-1)
            l1.append(x)
            j+=1
        i+=1
    print(l1)
    
list_fact([2,3,4])
    