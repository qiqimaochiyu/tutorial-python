#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:47:08 2018

@author: macbook
"""

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.d[key] = val
        return 

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        s = 0
        for i,val in self.d.items():
            if i.startswith(prefix):
                s += val
        return s
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)