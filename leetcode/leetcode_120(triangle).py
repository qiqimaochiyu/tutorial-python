class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        minsum = triangle[-1]
        for l in range(n-1)[::-1]:
            for i in range(l+1):
                minsum[i] = min(minsum[i], minsum[i+1]) + triangle[l][i]
        return minsum[0]
