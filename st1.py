# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:31:48 2018

@author: Bhaskar_Kishore
"""

shoplist=[]
add=input("want to shopping:y or n:")
while add.lower()=='y':
    item=input("enter your item to the list:")
    shoplist.append(item)
    add=input("want to shopping:y or n:")
print()
shoplist.sort()
for listitem in shoplist:
    print(listitem)    
    
    
d={'bannan':1,'apple':2,'orange':3}
#Matrix addition
a=int(input("enter no.of rows:"))
b=int(input("enter no.of columns:"))
x= [[input("enter the elements of mat1:") for j in range(b)]for i in range(a)]
y= [[input("enter the elements of mat2:") for j in range(b)]for i in range(a)]
result = [[int(x[i][j]) + int(y[i][j]) for j in range(0,b)] for i in range(0,a)]
print(result)