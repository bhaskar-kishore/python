# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 08:09:17 2018

@author: Bhaskar_Kishore
"""

import matplotlib.pyplot as plt
import pandas as pd
d=[[1,54,87],
   [2,85,35],
   [3,56,98],
   [4,89,75],
   [5,66,65],
   [6,88,86],
   [7,45,65],
   [8,80,78],
   [9,90,65],
   [10,58,85]]
e=pd.DataFrame(d,columns=['s.no','mathmetics','science'])
plt.scatter(e['mathmetics'],e['science'])
plt.show()


##2

import matplotlib.pyplot as plt
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range, math_marks, label='Math marks', color='c')
plt.scatter(marks_range, science_marks, label='Science marks', color='r')
plt.title('Scatter Plot')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()
