# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        res = []
        self.excute([root], res)
        return [float(sum(num))/len(num) for num in res ]
        
    def excute(self, now, res):
        if not now:
            return
        tmp = []
        next_tmp = []
        for one in now:
            tmp.append(one.val)
            if one.left:
                next_tmp.append(one.left)
            if one.right:
                next_tmp.append(one.right)
        res.append(tmp)
        self.excute(next_tmp, res)