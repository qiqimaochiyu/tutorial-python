#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:58:52 2018

@author: macbook
"""

class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int        
        找到达到目标点最小步数，第n步移动的距离为n，往左或往右都可以。
        这是一个偶函数，走到target和-target都是一样的，所以只考虑target>0
        的情况。
        1、如果能有n，使得sum = 1+2+...+n-1+n = target，显然，这是最佳
        方案。
        2、如果sum > target，需要前面有反方向走的
        2.1、delta = (sum - target) 是偶数，设第i,j...步往反方向走，
        那么最后到达的距离是: sum - 2*(i+j+...)，其中i, j...∈[1, n]，
        由于delta是偶数，必定存在i,j,...，使得2*(i+j+...) = delta。
        所以这种情况下，最佳步数还是n。
        2.2、delta = (sum - target) 是奇数，这样2.1情况下的i, j...
        找不到，需要加步数。所以最后到达的距离是: sum - 2*(i+j+...) 
        + n+1 + n+2 +...+ n+k ，现在需要找出最小的k。显然，
        k需要满足的条件是：使 sum + n+1 + n+2 +...+ n+k - delta
        为偶数，即 n+1 + n+2 +...+ n+k 为奇数，
        这样就能找到符合条件的i,j,...。所以，当n是偶数时，n+1就是奇数，
        只需要加1步；否则，加2步。
        """
        i = 0
        x = 0
        target = abs(target)
        if target == 2:
            return 3
        while x<target:
            x += i+1
            i += 1
        if x == target:
            return i
        else:
            if (x-target)%2 == 0:
                return i
            else:
                if i%2==0:
                    return i+1
                else:
                    return i+2
            
A = Solution()

print(A.reachNumber(11))