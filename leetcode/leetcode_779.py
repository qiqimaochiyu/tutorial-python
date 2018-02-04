class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        s = self.Gram(N)
        return int(s[K-1])
    def Gram(self, k):
        d = {'0':'01','1':'10'}
        if k== 1:
            return '0'
        s = map(lambda x:d[x], self.Gram(k-1))
        l = ''
        for i in s:
            l += i
        return l
    
