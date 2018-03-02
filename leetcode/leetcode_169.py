class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        max = 0
        this_max = 0
        for i in l:
            this_max += i
            if this_max > max:
                max = this_max
            if this_max < 0:
                this_max = 0
        return max
