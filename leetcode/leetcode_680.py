class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = len(s)
        i = 0
        while i < num // 2 and s[i] == s[-(i+1)]:i += 1
        s = s[i:num-i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]
