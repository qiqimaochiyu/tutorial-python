#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:53:45 2018

@author: macbook
"""

class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        L = []
        for i in range(len(A)):
            l = A[i:] + A[:i]
            L.append(self.countsum(l))
        return max(L)
        
    def countsum(self,l):
        s = 0            
        for i, j in enumerate(l):
            s += i * j
        return s
