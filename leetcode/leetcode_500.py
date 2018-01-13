#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:20:31 2018

@author: macbook
500. Keyboard Row

Given a List of words, return the words that can be typed using
 letters of alphabet on only one row's of American keyboard like the image below.
"""

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        m = set('qwertyuiop')
        n = set('asdfghjkl')
        t = set('zxcvbnm')
        l=[]
        for word in words:
            a=set(word.lower())
            if a&m==a or a&n==a or a&t==a:
                l.append(word)
        return l    
A=Solution()
words=["Hello", "ALaska", "Dad"]
print(A.findWords(words))