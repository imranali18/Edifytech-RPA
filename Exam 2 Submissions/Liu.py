# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:18:47 2019

@author: mushtu
"""

a=input('the list')
a=list(a)
b=[]
for i in range(len(a)):
    c=a[i]*i
    b.append(c)