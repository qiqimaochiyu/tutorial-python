# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        if not preorder:return None
        res = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        left_in = inorder[:index]
        right_in = inorder[index+1:]
        left_pre = preorder[1:len(left_in)+1]
        right_pre = preorder[len(left_in)+1:]
        res.left = self.buildTree(left_pre, left_in)
        res.right = self.buildTree(right_pre, right_in)
        return res
        """
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root
