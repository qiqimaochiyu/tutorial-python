#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:07:14 2018

@author: macbook
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None


class Solution:
    """
    @param: root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here
        if not root:
            return root
        s = TreeNode(root)
        s.val = root.val
        s.left = self.cloneTree(root.left)
        s.right = self.cloneTree(root.right)
        return s
    
