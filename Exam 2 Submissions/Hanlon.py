# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:51:18 2019

@author: mushtu
"""
list1=[2,3,4,5,8]
factorial = 1
j=1
i=0
while i < (len(list1)):
    while j <i:
        mult=list1[i]-j
        factorial = factorial * mult
print(factorial)