# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:return []
        def node(val, left, right):
            node = TreeNode(val)
            node.val = val
            node.left = left
            node.right = right
            return node
        def buildBST(begin, end):
            return [node(root, left, right) 
                   for root in range(begin, end+1)
                   for left in buildBST(begin, root-1)
                   for right in buildBST(root+1, end)] or [None]
        return buildBST(1,n)
