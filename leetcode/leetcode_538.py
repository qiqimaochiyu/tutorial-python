# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = []
        def travel(root):
            if root:
                travel(root.left)
                res.append(root.val)
                travel(root.right)
        travel(root)
        self.s = 0
        def travel2(root):
            if root:
                travel2(root.right)
                self.s += res.pop()
                root.val = self.s
                travel2(root.left)
        travel2(root)
        return root
