# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:28:24 2019

@author: mushtu
"""

nums=[1,2,3]
for i in range(len(nums)):
    j=nums[i]+nums[i+1]
    answer=j//len(nums)
print(answer)

def list_fact(nums):
    new_list=[]
    i=0
    while i in range(len(nums)):
        count=1
        for j in range(i):
            count=count*(i+1)
            new_list.append(count)
    print(new_list)
    
list_fact([2,3,4,5,8])
