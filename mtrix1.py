# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 22:32:52 2018

@author: Bhaskar_Kishore
"""

a=int(input("enter the row:"))
b=int(input("enter the column:"))
c=[[input("enter the elements matrix1:")for j in range(b)] for i in range(a)]
d=[[input("enter the elementsmatrix2:")for j in range(b)] for i in range(a)]
#e=[[0 for j in range(b)] for i in range(a)]

'''for i in range(a):
    for j in range(b):
        print(c[i][j])
        
for i in range(a):
    for j in range(b):
        print(d[i][j])
        
for i in range(a):
    for j in range(b):
        e=int[[int(c[i][j]+d([i][j])]for j in range(0,b)]for i in range(0,a)]'''
    
    
    
    
    

a=int(input("enter no.of rows:"))
b=int(input("enter no.of columns:"))
x= [[input("enter the elements of mat1:") for j in range(b)]for i in range(a)]
y= [[input("enter the elements of mat2:") for j in range(b)]for i in range(a)]
r = [[int(x[i][j]) + int(y[i][j]) for j in range(0,b)] for i in range(0,a)]
print(r)


#Matrix mul
a=int(input("enter no.of rows:"))
b=int(input("enter no.of columns:"))
x= [[input("enter the elements of mat1:") for j in range(b)]for i in range(a)]
y= [[input("enter the elements of mat2:") for j in range(b)]for i in range(a)]
r = [[int(x[i][j]) * int(y[i][j]) for j in range(0,b)] for i in range(0,a)]
print(r)

#Matrix sub
a=int(input("enter no.of rows:"))
b=int(input("enter no.of columns:"))
x= [[input("enter the elements of mat1:") for j in range(b)]for i in range(a)]
y= [[input("enter the elements of mat2:") for j in range(b)]for i in range(a)]
r = [[int(x[i][j]) - int(y[i][j]) for j in range(0,b)] for i in range(0,a)]
print(r)