class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        A = bytes(A)
        B = bytes(B)
        for length in range(len(A) + 1):
            if not any(A[i:i+length] in B for i in range(len(A) - length + 1)):
                return length - 1
        return length
