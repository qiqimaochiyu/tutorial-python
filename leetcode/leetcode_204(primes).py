 class Solution:
    def countPrimes(self, n):
        """
		初始所有一个n维数组 res 表示数都为素数。
		从3开始将3的奇数倍标记成False，即不是素数。
		之后对每一个素数此行上一步操作
		这里我们不用管偶数倍，因为我们最后判定时默认所有偶数不是素数
        """
        if n < 3:return 0
        res = [True] * n
        for i in range(3, int(n**0.5)+1, 2):
            res[i*i::2*i] = [False] * ((n-i*i-1)//(2*i)+1)
        return [2] + [i for i in range(3,n,2) if res[i]]
