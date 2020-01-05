# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:43:41 2019

@author: mushtu
"""

def list_fact(nums):
    new=[]
    count=1
    for num in nums:
        while count < nums:
            a=count*num
            new.append(a)
            count+=1
    print(new)
    
list_fact([2,3,4,5,8])
