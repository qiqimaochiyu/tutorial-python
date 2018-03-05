# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:return None
        m = len(nums) // 2 
        L = TreeNode(nums[m])
        L.left = self.sortedArrayToBST(nums[:m])
        L.right = self.sortedArrayToBST(nums[m+1:])
        return L
