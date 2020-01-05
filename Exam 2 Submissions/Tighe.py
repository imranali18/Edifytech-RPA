# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:00:41 2019

@author: mushtu
"""
def factorial(x):
    for i in x:
        fact=x[i]*range(x)
    
factorial([1,2,3,4])


x=0
values=[1,2,3,4]
for i in range(len(values)):
    values[i]=x*values[i]
    x+=1
print(values)