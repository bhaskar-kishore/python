# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:38:56 2018

@author: Bhaskar_Kishore
"""

n =input("read the sentence:")


dir(__builtins__)


n=n.lower()
print(n)

#n=n.upper()
#print(n)

n=n.replace('a','A')
n=n.replace('e','E')
n=n.replace('i','I')
n=n.replace('o','O')
n=n.replace('u','U')
print(n)

print(n[::-1])