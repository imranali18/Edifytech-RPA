# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:13:18 2019

@author: mushtu
"""

def list_factorial(nums):
    count=1
    for i in range((nums)):
        count=count*(i+1)
    return count

list_factorial([2,3,4,5,8])