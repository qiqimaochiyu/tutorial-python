class Solution:
    _r = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = self._r
        while len(r) <= n :
            r += min(r[len(r)-i*i]+1 for i in range(1, int(len(r)**0.5)+1)),
        return r[n]
