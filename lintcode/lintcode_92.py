class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        # write your code here
        n = len(A)
        dp = [[0 for _ in range(m+1)] for _ in range(2)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if j >= A[i-1]:
                    dp[i%2][j] = max(dp[(i-1)%2][j], dp[(i-1)%2][j-A[i-1]]+A[i-1])
                else:
                    dp[i%2][j] = dp[(i-1)%2][j]
        return max(i[-1] for i in dp)
