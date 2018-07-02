# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 09:47:11 2018

@author: Bhaskar_Kishore
"""
import matplotlib.pyplot as plt
languages=['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors=["blue","black","yellow","red","orange","violet"]
explode=(0.1,0,0,0,0,0)
plt.pie(popularity,explode=explode,labels=languages,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("The popularity of programming Languages",color='b')
plt.axis('equals')
plt.show()