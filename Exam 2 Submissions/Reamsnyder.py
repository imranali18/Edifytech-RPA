# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:38:27 2019

@author: mushtu
"""

def list_fact(list):
    sol=[]
    x=0
    for i in list:
        for s in range(1,i+1):
            x*=s
        sol.append(x)
    print(sol)

list_fact([2,3,4,5,8])

def power(list):
    sol=[]
    for i in list:
        x=i**(list.index(i))
        sol.append(x)
    print(sol)
    
power([1,2,3,4])
