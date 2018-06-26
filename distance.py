# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:39:16 2018

@author: Bhaskar_Kishore
"""

#distance speed time
s=int(input("enter the speed:"))
t=int(input("enter the time:"))
#miles to covert in km
miles=(s*1.609344)
#meters to convert in km
meter=s*18/5
d=miles*t
e=meter*t
print("distance is",d,'km/h')
print("distance is",e,'km/h')