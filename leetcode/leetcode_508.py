# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        def getSum(root):
            if not root:return 0
            s = root.val + getSum(root.left) + getSum(root.right)
            d[s] = d.get(s, 0) + 1
            return s
        d = {}
        getSum(root)
        frequence = max(d.values())
        return [i for i in d.keys() if d[i] == frequence]
