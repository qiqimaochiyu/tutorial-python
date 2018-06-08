class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(1+m)]
        if m==0 and n==0 and len(s3)==0:dp[0][0]=1 
        for i in range(m):
            if s1[i]==s3[i]:
                dp[i+1][0]=1
            else:
                break
        for j in range(n):
            if s2[j]==s3[j]:
                dp[0][j+1]=1
            else:
                break
        for i in range(1,m+1):
            for j in range(1,n+1):
                if dp[i-1][j] and s1[i-1]==s3[i+j-1] or dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                        dp[i][j]=1
                else:
                    dp[i][j]==0
        return bool(dp[m][n])
