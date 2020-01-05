# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:03:38 2019

@author: mushtu
"""
def list_fact(l1):
    newlist=[]
    i=0
    while i <len(l1):
        x=1
        y=int(l1[i])
        while x<=y:
            if y%x==0:
                newlist.append(x)
            x+=1
        i+=1
    print(newlist)
    
    
list_fact([2,3,4,5,8])
