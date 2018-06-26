# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:40:10 2018

@author: Bhaskar_Kishore
"""

a=int(input("enter no.of rows:"))
b=int(input("enter no.of columns:"))
x= [[input("enter the elements of mat1:") for j in range(b)]for i in range(a)]
y= [[input("enter the elements of mat2:") for j in range(b)]for i in range(a)]
r = [[int(x[i][j]) * int(y[i][j]) for j in range(0,b)] for i in range(0,a)]
print(r)