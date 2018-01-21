#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:12:25 2018

@author: macbook

Given a string S, check if the letters can be rearranged
 so that two characters that are adjacent to each other
 are not the same.

If possible, output any possible result.  If not possible, 
return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
"""
from collections import Counter  
import heapq  
  
class Solution:  
    def reorganizeString(self, S):  
        """ 
        :type S: str 
        :rtype: str 
        """  
        ret = ''  
        pq = []  
        c = Counter(S)  
        for k, v in c.items():  
            heapq.heappush(pq, (-v, k))  
          
        # previous key value  
        prev_v, prev_k = 0, ''  
        while pq:  
            v, k = heapq.heappop(pq)  
            ret += k  
            if prev_v<0:  
                heapq.heappush(pq, (prev_v, prev_k)) # delay one loop to prevent aab  
            prev_v, prev_k = v+1, k    # store current key value for latter enqueue  
              
        return ret if len(ret)==len(S) else ''
    
    