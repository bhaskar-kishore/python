# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 18:50:32 2018

@author: Bhaskar_Kishore
"""

time = int(input("Input time in seconds: "))

time %=  (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("h:m:s-> %d:%d:%d" %( hour, minutes, seconds))
