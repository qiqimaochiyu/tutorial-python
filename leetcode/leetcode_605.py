class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        f = [0] + flowerbed + [0]
        for i in range(len(f)-2):
            if f[i] == 0 and f[i+1] == 0 and f[i+2] == 0:
                f[i+1] = 1
                n -= 1
        return  n <= 0
