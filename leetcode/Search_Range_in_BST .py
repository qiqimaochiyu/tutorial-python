"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        if not root:
            return []
        if k1 > root.val:
            return self.searchRange(root.right, k1, k2)
        if k2 < root.val:
            return self.searchRange(root.left, k1, k2)
        else:
            return self.searchRange(root.left, k1, root.val) + [root.val] + self.searchRange(root.right, root.val, k2)
