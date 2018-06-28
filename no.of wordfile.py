# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:26:23 2018

@author: Bhaskar_Kishore
"""

fname = input("Enter file name: ")  
num = 0   
with open(fname, 'r') as f:  
     for line in f: 
         words = line.split() 
         num += len(words) 
print("Number of words:") 
print(num)
print(words)





    