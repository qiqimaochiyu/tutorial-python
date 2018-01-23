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
        ## 复杂度O（n^2）
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

            n=len(A)
        if n==0:
            return 0
        
    def maxRotateFunction2(self, A):
        ## 复杂度 O（n）
        s=0
        sA=0
        for i in range(n):
            s+=A[i]*i
            sA+=A[i]
        maxf=s
        for i in range(1,n):
            s=s+sA-n*A[n-i]
            maxf=max(maxf,s)
        return maxf
