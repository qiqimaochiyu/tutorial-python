class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import Counter
        m, n = len(s1), len(s2)
        cur, target = Counter(s2[:m]), Counter(s1)
        if cur == target: return True

        for i in range(n-m):
            cur[s2[i]] -= 1
            cur[s2[m+i]] += 1
            cur += Counter()
            if cur == target: return True
        return False
