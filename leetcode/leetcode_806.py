class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        res = 0
        line = 1
        for s in S:
            num = widths[ord(s)-97]
            if res + num <= 100:
                res += num
            else:
                res = num
                line += 1
        return [line, res]
        
