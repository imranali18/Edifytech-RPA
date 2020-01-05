# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:32:05 2019

@author: mushtu
"""

n=int(input('enter number '))
for i in range(1,n,1):
    if n%i==0:
        print(i)
        
        
def find_pal(a):
    list1=[]
    for i in range(len(a)):
        b=a[i]
        if b.reverse==a[i]:
            list1.insert('True')
        else:
            list1.insert('False')
            
find_pal(['abc','nursesrun','mom'])
