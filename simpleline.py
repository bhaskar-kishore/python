# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 19:38:51 2018

@author: Bhaskar_Kishore
"""

import matplotlib.pyplot as plt
x1 = [1,2,3]
y1 = [2,4,1]
plt.plot(x1, y1, label = "line 1")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('single line on sgraph!')
plt.xlim(1,10),plt.xticks([])
plt.ylim(1,10),plt.xticks([])

plt.legend()
plt.show()
plt.savefig('C:\\Users\\Bhaskar_Kishore\\Desktop\\solve\\t.jpeg')
plt.show()