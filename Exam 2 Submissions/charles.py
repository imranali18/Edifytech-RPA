# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:14:47 2019

@author: mushtu
"""

list_fact=input("Enter:  ")
x=list_fact
y=1
z=[]
while y <=x:
    if x*y==0:
        z.append(y)
    y+=1
print (z)
    