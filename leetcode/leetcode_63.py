class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ob = obstacleGrid
        n, m = len(ob[0]), len(ob)
        a = [[0 for i in range(n)] for j in range(m)]
        i = 0
        while i < n and ob[0][i] != 1:
            a[0][i] = 1
            i += 1
        j = 0
        while j < m and ob[j][0] != 1:
            a[j][0] = 1
            j += 1
        for p in range(1, m):
            for q in range(1, n):
                if ob[p][q] == 1:
                    a[p][q] = 0
                else:
                    a[p][q] = a[p-1][q] + a[p][q-1]
        return a[-1][-1]