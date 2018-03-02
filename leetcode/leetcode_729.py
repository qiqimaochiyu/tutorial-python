class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        s0, s1 = 0, -float('inf')
        for p in prices:
            s0, s1 = max(s0, s1+p), max(s1, s0-p-fee)
        return s0
        
