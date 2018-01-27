class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        L = []
        m, n = len(s), len(p)
        cur, target = Counter(s[:n]), Counter(p)
        if cur == target:
            L.append(0)
        for i in range(m-n):
            cur[s[i]] -= 1
            cur[s[n+i]] += 1
            cur += Counter()
            if cur == target:
                L.append(i+1)
        return L