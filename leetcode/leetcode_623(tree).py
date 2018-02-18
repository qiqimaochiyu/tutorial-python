class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        res, res.left = TreeNode(None), root
        row = [res]
        for _ in range(d-1):
            row = [kid for r in row for kid in (r.left, r.right) if kid]
        for r in row:
            r.left, r.left.left = TreeNode(v), r.left
            r.right, r.right.right = TreeNode(v), r.right
        return res.left
