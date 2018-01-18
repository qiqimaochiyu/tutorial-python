#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:12:10 2018

@author: macbook

Given a non-negative integer num, repeatedly add all its digits
until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
Since 2 has only one digit, return it.
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = num % 10 + num // 10
        return int(num)
    
    
A = Solution()
num=18
print(A.addDigits(num))

