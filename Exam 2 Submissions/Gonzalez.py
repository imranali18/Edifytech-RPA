# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:24:45 2019

@author: mushtu
"""

def list_fact(x):
    c=1
    out=[]
    for i in range(len(x)):
        c=c*x[i+1]
        out.append(c)
    return c

list_fact([2,3,4,5,8])


list1=[1,2,3]
i=0
index(list1[i])
