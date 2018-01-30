# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        s = TreeNode(root)
        if not root:
            return
        s.val = root.val
        s.left = self.invertTree(root.right)
        s.right = self.invertTree(root.left)
        return s
