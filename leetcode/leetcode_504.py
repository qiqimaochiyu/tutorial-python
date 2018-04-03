class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        L = []
        n = abs(num)
        while n >= 7:
            L.append(str(n % 7))
            n = n // 7
        L.append(str(n))
        return "".join(L[::-1]) if num >= 0 else "-"+"".join(L[::-1])
