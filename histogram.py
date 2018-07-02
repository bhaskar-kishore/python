# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 19:59:15 2018

@author: Bhaskar_Kishore
"""

import matplotlib.pyplot as plt
import numpy as np
g= np.random.randn(1000)
plt.hist(g)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")



