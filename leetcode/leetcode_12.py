#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:15:21 2018

@author: macbook
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in enumerate(values):
            res += (num//v) * numerals[i]
            num %= v
        return res
        