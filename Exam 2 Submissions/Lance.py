# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:38:40 2019

@author: mushtu
"""

def factorial(nums):
    count=0
    for i in range(nums):
        count=count*(i+1)
    return count

factorial([2,3,4,5])
