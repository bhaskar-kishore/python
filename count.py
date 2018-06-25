# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 17:52:33 2018

@author: Bhaskar_Kishore
"""

b=input("enter read :")
vowels=['a','e','i','o','u']
for x in b.lower():
    if x in vowels :
        b=b.replace(x,"")
print(b)

c=input("enter read :")
c=c.replace('v','b')
#c=c.replace('b','v',3)
print(c)

print(len(b))

d=input("enter data:")
#word=d.split()
wordCount=len(d)
print(wordCount)