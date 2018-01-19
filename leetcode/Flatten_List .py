#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:42:34 2018

@author: macbook
"""

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        L = []
        if type(nestedList) == int:
            return [nestedList]
        for i in list(nestedList):
            if type(i)==list:
                L += self.flatten(list(i))
            else:
                L.append(i)
        return L
print(Solution().flatten(10) )



### 使用yield from 递归生成器处理

from collections import Iterable

class Solution2(object):
    
    def flatten(self, items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                yield from self.flatten(x)
            else:
                yield x
    

items = [1, 2, [3, 4, [5, 6], 7], 8]
L = []
s = Solution2().flatten(items)
for x in s:
    L.append(x)
print(L)