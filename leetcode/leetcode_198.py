#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:20:37 2018

@author: macbook

House Robber
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t1, t2 = 0, 0
        for i in nums:
            t1, t2 = t2, max(t1+i, t2)
        return t2