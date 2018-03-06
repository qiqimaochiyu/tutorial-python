class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for i in set(s):
            if s.count(i) < k:
                return max(self.longestSubstring(m, k) for m in s.split(i))
        return len(s)
        
