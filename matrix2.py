# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 23:27:25 2018

@author: Bhaskar_Kishore
"""
from operator import add
list1=[1,2,3]
list2=[4,5,6]
       
list(map(add,zip(list1,list2)))
#[sum(x) for x in zip(list1,list2)]

stack=[1,2,3]
stack.append(4)
print(stack)
stack.pop()
print(stack.pop())
print(stack)

from collections import deque
queue=deque([1,2,3])
queue.pop()
print(queue)

from operator import add
l1=[12,1,2]
l2=[5,6,3]
list(map(add,zip(l1,l2)))

