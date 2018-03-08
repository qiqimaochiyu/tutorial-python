class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = [0] * n
        for i in range(n):
            if i % 2 == 0:
                res[i] = n - i // 2
            else:
                res[i] = i // 2 + 1
        if k%2==0:
            return res[:k-1] + sorted(res[k-1:])
        else:
            return res[:k] + sorted(res[k:], key=lambda x:-x)
