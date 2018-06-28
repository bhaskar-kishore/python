# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:44:07 2018

@author: Bhaskar_Kishore
"""

def triple(arr,n):
    f=True
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(arr[i]+arr[j]+arr[k]==0):
                    print(arr[i],arr[j],arr[k])
                f=True
    if(f==False):
        print("not exist")