# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 10:05:20 2018

@author: Bhaskar_Kishore
"""

import matplotlib.pyplot as plt
languages=['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7]
#colors=["blue","black","yellow","red","orange","violet"]
xs = [i + 0.1 for i, _ in enumerate(languages)]
plt.bar(xs,popularity)
plt.xticks([i + 0.1 for i, _ in enumerate(languages)],languages)
plt.title("The popularity of programming Languages",color='y')
plt.show()