# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:28:54 2019

@author: mushtu
"""

def list_fact(L):
    for i in L:
        j=i
        k=1
        while j>0:
            k*=j
            j-=1
    print(k)
    
list_fact([2,3,4,5,8])

list1=[1,2,3,4]
newlist=[]
for i in list1:
    k=list1.index(i)
    newval=i**k
    newlist.append(newval)
print(newlist)
