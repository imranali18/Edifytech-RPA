# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:31:08 2019

@author: mushtu
"""

def list_fact(array):
    factorials=[]
    for j in range(0,len(array)):
        x=1
        x=array[j]*x
        factorials.append(x)
    return factorials
    
list_fact([2,3,4,5,8])
