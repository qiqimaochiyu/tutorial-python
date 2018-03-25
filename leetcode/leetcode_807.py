class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row = [max(cow) for cow in grid]
        max_column = [max(i) for i in [[cow[i] for cow in grid] for i in range(len(grid[0]))]]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res += min(max_row[i], max_column[j]) - grid[i][j]
        return res
