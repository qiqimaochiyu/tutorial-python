# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(r, l):
            if r and l and r.val == l.val:
                return isSym(r.left, l.right) and isSym(r.right, l.left)
            return r==l
        return isSym(root, root)
                