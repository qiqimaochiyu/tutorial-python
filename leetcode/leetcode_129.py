# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path = ''
        res = []
        self.TreePathhelp(root, path, res)
        return sum([int(i) for i in res])
        
    def TreePathhelp(self, root, path, res):
        if not root:return
        path += str(root.val)
        if root.left:
            self.TreePathhelp(root.left, path, res)
        if root.right:
            self.TreePathhelp(root.right, path, res)
        if not root.left and not root.right:
            res.append(path)
