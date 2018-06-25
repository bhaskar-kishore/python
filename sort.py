# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 22:16:48 2018

@author: Bhaskar_Kishore
"""

'''A = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]'''
A=int(input("enter the row:"))
B=int(input("enter the column:"))
# take a 3x4 matrix 
'''B = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]'''
c=[[input("enter the elements matrix1:")for j in range(B)] for i in range(A)]
d=[[input("enter the elementsmatrix2:")for j in range(B)] for i in range(A)]
#result=[[0 for j in range(B)] for i in range(A)]
result = [[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]]

# iterating by row of A
for i in range(len(0,A)):

	# iterating by coloum by B 
	for j in range(len(B[0])):

		# iterating by rows of B
		for k in range(len(0,B)):
			result[i][j] += A[i][k] * B[k][j]

for r in result:
	print(r)
