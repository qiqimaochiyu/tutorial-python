res = {}
class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def count(i, X):
            if i==1:
                return 1
            key = (i, X)
            if key in res:
                return res[key]
            total = sum(count(i-1, X[:j]+X[j+1:]) for j, x in enumerate(X) if x%i==0 or i%x==0)
            res[key] = total
            return total
        return count(N, tuple(range(1,N+1)))
