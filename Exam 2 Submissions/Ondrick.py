# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:05:45 2019

@author: mushtu
"""

def list_avg(nums):
    i=0
    while i < len(nums):
        y=nums[i]+nums[i+1]
        i+=1
    x=y/(len(nums)+1)
    print(x)
    
list_avg([3,4,5])

def list_fact(nums):
    new_list=[]
    x=nums[1]