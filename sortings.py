# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:27:43 2018

@author: Bhaskar_Kishore
"""

t1=(1,2,3)
t2=(4,5,6)
nt=(t1,t2)
print(nt)


def bubblesort(list):
# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)