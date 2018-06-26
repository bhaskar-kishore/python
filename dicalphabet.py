# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:22:58 2018

@author: Bhaskar_Kishore
"""

d={'Mexico':'MexicoCity','China':'Beijing','France':'Paris','Belgium':'Brussels','Argentina':'Buenos'}       
v=sorted(d.keys())
for key in v:
    print("%s: %s" %(key, d[key])) 