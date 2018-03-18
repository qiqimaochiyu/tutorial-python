class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        # iterate
        if k == 0:return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
        """
        # recursion
        res = [[]]
        for _ in range(k):
            res = [[i] + c for c in res for i in range(1, c[0] if c else n+1)]
        return res
