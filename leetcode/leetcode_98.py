# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, left=float('-inf'), right=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or left < root.val < right and \\
        self.isValidBST(root.left, left, root.val) and \\
        self.isValidBST(root.right, root.val, right)
