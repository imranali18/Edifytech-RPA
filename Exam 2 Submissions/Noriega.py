# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:53:10 2019

@author: mushtu
"""

def list_fact(listnum):
    i=0
    newnum=[]
    while i <len(listnum):
        newnum[i]=listnum[i]
        i+=1
    print(newnum)

list_fact([2,3,4,5,8])


def explist(list1):
    i=0
    newlist=[]
    while i < len(list1):
        newlist[i]=list[i]**i
        i+=1
    return newlist

explist([1,2,3,4])
