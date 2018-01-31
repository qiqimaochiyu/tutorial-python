class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon[0])
        need = [2**31] * (n-1) + [1]
        for row in dungeon[::-1]:
            for i in range(n)[::-1]:
                need[i] = max(min(need[i:i+2]) - row[i], 1)
        return need[0]
