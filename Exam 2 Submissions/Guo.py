# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:15:53 2019

@author: mushtu
"""

def factorial(x):
    list1=[]
    count=1
    for i in range(len(x)):
        a=x[i]
        for j in range(a):
            count=count*(1+j)
        list1.append(count)
    print (list1)
    
factorial([2,3,4,5,8])

list1=[1,2,3,4]
list2=[]
for (i,v) in enumerate(list1):
    a=v**i
    list2.append(a)
print(list2)