# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:54:55 2019

@author: mushtu
"""

def list_fact(x):
    count=1
    for i in range(len(x)):
        count=count*(i+1)
    return count

list_fact([2,3,4,5,8])
