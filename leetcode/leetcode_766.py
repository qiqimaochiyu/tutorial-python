#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:44:40 2018

@author: macbook
"""

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)-1):
            if matrix[i][:-1] == matrix[i+1][1:]:
                continue
            else:
                return False
        return True