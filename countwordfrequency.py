# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:56:31 2018

@author: Bhaskar_Kishore
"""

#file=open('bhaskar.txt')
fname = input("Enter file name: ")  
with open(fname, 'r') as file:  
    text=file.read().split()
mydict={}
for word in text:
    if word not in mydict.keys():
        mydict[word]=1
    else:
        count=mydict[word]
        mydict[word]=count+1
print(mydict)