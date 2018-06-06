class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        import string
        dic = {c:[-1,-1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = dic[c]
            res += (i - j) * (j - k)
            dic[c] = [j, i]
        for c in dic:
            k, j = dic[c]
            res += (len(S)-j)*(j-k)
        return res%(10**9+7)
