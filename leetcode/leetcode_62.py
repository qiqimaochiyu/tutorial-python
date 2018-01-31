# math method

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = min(m, n)
        b = m + n - 2
        def f(k):
            return reduce(lambda x,y:x*y,[1]+range(1,k+1))
        return f(b)/(f(a-1)*f(b-a+1))
        
# dp method


class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]
