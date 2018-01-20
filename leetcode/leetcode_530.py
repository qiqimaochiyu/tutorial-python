# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue=[root];l=[root.val]
        while queue:
            node=queue.pop()#node等于退出的一个节点
            if node.left:
                queue.append(node.left)
                l.append(node.left.val)
            if node.right:
                queue.append(node.right)
                l.append(node.right.val)
        answer=[];sortedl=sorted(l)
        for i in range(1,len(sortedl)):
            answer.append(sortedl[i]-sortedl[i-1])
        return min(answer)