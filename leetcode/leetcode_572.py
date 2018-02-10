class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def sameTree(s, t):
            if not s and not t:return True
            if not s or not t:return False
            return s.val == t.val and sameTree(s.left, t.left) and sameTree(s.right, t.right)
            
        if sameTree(s, t):return True
        if not s:return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) 
