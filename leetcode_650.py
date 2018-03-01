class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        for i in range(2,n+1):
            while n % i == 0:
                s += i
                n = n // i
        return s
            
