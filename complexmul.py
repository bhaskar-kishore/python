# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:08:03 2018

@author: Bhaskar_Kishore
"""

import numpy as np
x=np.array([[1+2j,2+3j]])
y=np.array([[2+5j,6+7j]])
z=np.vdot(x,y)
print(z)
