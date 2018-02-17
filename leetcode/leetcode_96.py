class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 1]
        for i in range(2, n+1):
            res += sum([res[j-1]*res[i-j] for j in range(1, i+1)]),
        return res[-1]
