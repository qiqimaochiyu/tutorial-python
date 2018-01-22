#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:53:27 2018

@author: macbook
"""

class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n//2)+1
        else:
            return min(self.integerReplacement(n-1)+1,self.integerReplacement(n+1)+1)
        