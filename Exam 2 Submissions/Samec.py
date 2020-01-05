# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:30:46 2019

@author: mushtu
"""


def list_fact(num):
    list1=[2,3,4,5,8]
    list2=[]
    for num in list1:
        count=1
        for i in range(num):
            count=count*(i+1)
        return count
        list1.append(count)
    return list1

list_fact([2,3,4,5,8])
    