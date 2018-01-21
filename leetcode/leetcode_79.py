#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:19:18 2018

@author: macbook
"""

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        l = len(word)
        if l == 0:
            return False
        m = len(board)
        if m == 0: return False
        n = len(board[0])
        visit = [[False for i in range(n)] for j in range(m)]
        def dfs(x,y,word):
            if len(word) == 0: return True
            if x > 0 and not visit[x-1][y] and board[x - 1][y] == word[0]:
                visit[x - 1][y] = True
                if dfs(x - 1,y,word[1:]):
                    return True
                visit[x - 1][y] = False
            if y > 0 and not visit[x][y-1] and board[x][y-1] == word[0]:
                visit[x][y-1] = True
                if dfs(x,y-1,word[1:]):
                    return True
                visit[x][y-1] = False
            if x + 1< m and not visit[x+1][y] and board[x+1][y] == word[0]:
                visit[x+1][y] = True
                if dfs(x+1,y,word[1:]):
                    return True
                visit[x+1][y] = False
            if y + 1 < n and not visit[x][y + 1] and board[x][y + 1] == word[0]:
                visit[x][y + 1] = True
                if dfs(x,y + 1,word[1:]):
                    return True
                visit[x][y + 1] = False
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visit[i][j] = True
                    if dfs(i,j,word[1:]):
                        return True
                    visit[i][j] = False
        return False