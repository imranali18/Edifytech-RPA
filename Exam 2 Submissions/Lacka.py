# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:14:54 2019

@author: mushtu
"""

avg=[3,4,5]
i=0
while i <len(avg):
    avg=avg[0]+avg[1]
    i+=1
    avg=avg/len(avg)
print(avg)

def list_fact(x):
    count=1
    for i in range(len(x)):
        count=count*(1+i)
    return count

list_fact([2,3,4])
