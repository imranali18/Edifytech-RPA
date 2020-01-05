# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:17:30 2019

@author: mushtu
"""


def list_fact(a):
    count=1
    l1=[]
    i=0
    while i<len(a):
        for count in range(a[i]):
            count=count*(i+1)
        l1.append(count)
        i+=1
    print(l1)
    
list_fact([2,3,4,5,8])


l1=[1,2,3,4]
l2=[]
i=0
while i < len(l1):
    a=l1[i]**i
    l2.append(a)
    i+=1
print(l2)