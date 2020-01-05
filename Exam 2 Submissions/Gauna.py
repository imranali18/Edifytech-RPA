# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:35:05 2019

@author: mushtu
"""
n=[3,4,5]
mean=0
for i in range(len(n)):
    i+=mean
    mean=mean/len(n)
print(mean)

def list_fact(n):
    k=[]
    for i in n:
        for x in range(len(n)):
            x=n*x
            k.append(x)
    print(k)
    
list_fact([2,3,4,5,8])
