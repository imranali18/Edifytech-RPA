# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:05:26 2019

@author: mushtu
"""

def list_fact(x):
    count=1
    blank=[]
    for i in range(len(x)):
        for j in range(i):
            y=count*(i+1)
            blank.append(y)
        count+=1
    return blank

list_fact([2,3,4,5,8])
