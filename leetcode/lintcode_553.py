#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:31:06 2018

@author: macbook

class Solution():
    
    
    def maxKilledEnemies(self, grid):
        # write your code here
        ans = 0
        for id1, m in enumerate(grid):
            for id2, n in enumerate(m):
                if n == '0':
                    ans = max(ans, self.count_E(id2, m) + self.count_E(id1, [g[id1] for g in grid]))
                    print(ans)
        return ans
    def count_E(self, index, L):
        if 'W' not in L:
            return L.count('E')
        else:
            res = 0
            i, j = index, index
            while i > 0:
                i -= 1 
                if L[i] == 'W':
                    break
                elif L[i] == 'E':
                    res += 1 
            #print(res)
            while j < len(L)-1:
                j += 1 
                if L[j] == 'W':
                    break
                elif L[j] == 'E':
                    res += 1 
            return res
        
        
a = Solution()
L = ["0E00","E0WE","0E00"]
print(a.maxKilledEnemies(L))


"""
class Solution():
    
    
    def maxKilledEnemies(self, grid):
        """
        # write your code here
        if not grid:return 0
        m, n = len(grid), len(grid[0])
        v1 = [[0 for _ in grid[0]] for _ in grid]
        v2 = [[0 for _ in grid[0]] for _ in grid]
        v3 = [[0 for _ in grid[0]] for _ in grid]
        v4 = [[0 for _ in grid[0]] for _ in grid]
        res = 0
        #print(m,n)
        for i in range(m):
            for j in range(n):
                t = 0 if j == 0 or grid[i][j] == 'W' else v1[i][j-1]
                v1[i][j] = t+1 if grid[i][j] == 'E' else t
            for j in range(n)[::-1]:
                t = 0 if j == n-1 or grid[i][j] == 'W' else v2[i][j+1]
                v2[i][j] = t+1 if grid[i][j] == 'E' else t
        for j in range(n):
            for i in range(m):
                t = 0 if i == 0 or grid[i][j] == 'W' else v3[i-1][j]
                v3[i][j] = t+1 if grid[i][j] == 'E' else t
            for i in range(m)[::-1]:
                t = 0 if i == m-1 or grid[i][j] == 'W' else v4[i+1][j]
                v4[i][j] = t+1 if grid[i][j] == 'E' else t
        print(v3)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, v1[i][j]+v2[i][j]+v3[i][j]+v4[i][j])
        return res
        """
        if not grid:return 0
        m, n = len(grid), len(grid[0])
        res, rowCnt= 0, 0
        colCnt = [0 for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    rowCnt = 0
                    for k in range(j, n):
                        if grid[i][k] != 'W':
                            rowCnt += (grid[i][k] == 'E')  
                        else:
                            break
                if i == 0 or grid[i-1][j] == 'W':
                    colCnt[j] = 0
                    for k in range(i, m):
                        if grid[k][j] != 'W':
                            colCnt[j] += (grid[k][j] == 'E') 
                        else:
                            break
                if grid[i][j] == '0':
                    res = max(res, rowCnt+colCnt[j])
        return res
        
        
a = Solution()
L=["W","0","0","0","0","0","E","E","E","E","E","E","E","E","0",
   "0","0","0","0","0","W","W","W","0","W","W","W","0","0","W",
   "0","W","0","W","E","E","E","E","0","0","0","0","E","W","0","0","W"]
print(a.maxKilledEnemies(L))
