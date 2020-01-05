# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:00:24 2019

@author: mushtu
"""
def list_facts(nums):
    #nums=[]
    count=1
    for i in range(len(nums), nums+1):
        count= count*(i+1)
        count+=1
    return count
   
list_facts([2,4,5])
