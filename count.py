# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 17:52:33 2018

@author: Bhaskar_Kishore
"""

b=input("enter read :")
vowels=['a','e','i','o','u','A','E','I','O','U']
for x in b:

        if x in vowels :
                b=b.replace(x,"")

print(b)



print(len(b))

d=input("enter data:")
#word=d.split()
wordCount=len(d)
print(wordCount)




###replacement
import re
d=input("enter read")
re.sub('.', lambda m: {'b':'v', 'v':'b'}.get(m.group(), m.group()), d)
