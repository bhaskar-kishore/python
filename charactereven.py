# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:37:56 2018

@author: Bhaskar_Kishore
"""

#x = "seMi Long StRing WiTH COMPLetely RaNDOM CasINg"
x=str(input("enter the string:"))
result_string = ""
index = 0;
for c in x:
    if(index%2 == 0):
        result_string += c.lower()
    else:
        result_string += c.upper()
    index+=1

print(result_string)