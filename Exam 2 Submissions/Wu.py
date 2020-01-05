# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:58:50 2019

@author: mushtu
"""

def list_fact(lst):
    sum=0
    for num in lst:
        sum+=num
    list_fact=sum*len(lst)
    return list_fact

x=[2,3,4,5,8]
print(list_fact(x))
