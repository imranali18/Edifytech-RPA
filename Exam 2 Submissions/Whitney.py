# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:46:49 2019

@author: mushtu
"""

def list_fact(nums):
    s=[]
    for i in range(len(nums)):
        mult=nums[i]-1
        while mult >0:
            x=nums[i]*mult
        s.append(x)
    print(s)
    
list_fact([2,3,4,5,8])
