# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:52:52 2019

@author: mushtu
"""

def list_fact(a):
    nl=[]
    i=0
    while i <len(a):
        fl=range(a[i])
        x=sum(fl)
        nl.append(x)
        i+=1
    print(nl)
    
list_fact([2,3,4,5,8])
