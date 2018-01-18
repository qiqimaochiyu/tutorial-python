#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:54:01 2018

@author: macbook
"""
import sys

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    Given an array with integers.

    Find two non-overlapping subarrays A and B, which |SUM(A) - SUM(B)| is the largest.

    Return the largest difference.         
             
    """
    def maxDiffSubArrays(self, nums):
        if not nums:
            return 0
            
        size = len(nums)
        leftMax, leftMin = [0 for i in range(size)], [0 for i in range(size)]
        rightMax, rightMin = [0 for i in range(size)], [0 for i in range(size)]
        maxRes, minRes, sum, minSum, maxSum = -sys.maxsize - 1, sys.maxsize, 0, 0, 0
        for i in range(size):
            sum += nums[i]
            maxRes = max(maxRes, sum - minSum)
            minSum = min(minSum, sum)
            leftMax[i] = maxRes
            minRes = min(minRes, sum - maxSum)
            maxSum = max(maxSum, sum)
            leftMin[i] = minRes
            
        maxRes, minRes, sum, minSum, maxSum = -sys.maxsize - 1, sys.maxsize, 0, 0, 0
        for i in range(size - 1, -1, -1):
            sum += nums[i]
            maxRes = max(maxRes, sum - minSum)
            minSum = min(minSum, sum)
            rightMax[i] = maxRes
            minRes = min(minRes, sum - maxSum)
            maxSum = max(maxSum, sum)
            rightMin[i] = minRes
        
        result = -sys.maxint - 1
        for i in range(size - 1):
            result = max(result, abs(leftMax[i] - rightMin[i + 1]), abs(leftMin[i] - rightMax[i + 1]))
            
        return result


    
    
    
    
    
    
        

