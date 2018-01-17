#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:28:42 2018

@author: macbook
"""

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        sum = {}
        L = []
        for i, m in enumerate(list1):
            if m in list2:
                sum[m]=i+list2.index(m)
        Mi = min(sum.values())
        for key, value in sum.items():
            if value==Mi:
                L.append(key)
        return L
                
                
A=Solution()
list1=["Shogun","Tapioca Express","Burger King","KFC"]
list2=["KFC","Burger King","Tapioca Express","Shogun"]
print(A.findRestaurant(list1,list2))
