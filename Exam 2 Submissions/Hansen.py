# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:01:19 2019

@author: mushtu
"""


def list_fact(x):
    count=1
    for i in range(x):
        count=count*(i+1)
    return count


list_fact([2,3,4,5,8])


def list1(nums):
    i=0
    while i<len(nums):
        new_list=(nums[i]**nums.index(i))
        i+=1
    return new_list
        
list1([1,2,3,4])
