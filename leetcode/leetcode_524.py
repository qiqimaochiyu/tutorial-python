# 妙用 生成器 iter（）
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        best = ''
        for x in d:
            if (-len(x), x) < (-len(best), best):
                it = iter(s)
                if all(c in it for c in x):
                    best = x
        return best
        
