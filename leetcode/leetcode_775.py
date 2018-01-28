class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n, i, m = len(A), n-3, A[-1]
        while i >= 0:
            if A[i] > m:
                return False
            m = min(m,A[i+1])
            i -= 1
        return True