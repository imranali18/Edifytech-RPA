# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:23:52 2019

@author: mushtu
"""

def avgnum(list1):
    for i in range(len(list1)):
        x=list1[i]+list1[i+1]
        y=int(x/len(list1))
    print(y)
    
avgnum([1,2,3])


def factorial(n):
    count = 1
    for i in range(n):
        count=count*(i+1)
    return count

def list_fact(nums):
    factnums=[]
    for n in range(len(nums)):
        solve=factorial(n)
        factnums.append(solve)
    print (factnums)
    
list_fact([2,5])

list1=[1,2,3,4]
count=0
for i in range(len(list1)):
    list1[i]=list1[i]**count
    count+=1
print(list1)
