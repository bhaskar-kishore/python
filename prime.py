# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:27:49 2018

@author: Bhaskar_Kishore
"""


n=int(input("enter the value:"))     
for num in range(2,n+1):
    for i in range(2,num):
        if ((num)%i==0):
            break
    else:
        print(num)       
        