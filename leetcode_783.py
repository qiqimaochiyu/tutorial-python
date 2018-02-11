# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

###########Minimum Distance Between BST Nodes############

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        L=[]
        def trimBST(L, node):
            if node.left:trimBST(L, node.left)
            L.append(node.val)
            if node.right:trimBST(L, node.right)
            return L
        L = trimBST(L, root)
        return min([L[i+1]-L[i] for i in range(len(L)-1)])
