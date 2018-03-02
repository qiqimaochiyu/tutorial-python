class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        
        r = [0] * (len(cost)+1)
        r[1] = cost[0]
        for i in range(2, len(cost)+1):
            r[i] = min(r[i-1]+cost[i-1], r[i-2]+cost[i-1])
        return min(r[-1], r[-2])
        """
        l1, l2 = cost[0], cost[1]
        for i in cost[2:]:
            l1, l2 = l2, min(l1, l2)+i
        return min(l1,l2)
