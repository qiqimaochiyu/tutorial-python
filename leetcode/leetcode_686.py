class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a = A
        i = 1
        while B not in a:
            a += A
            i += 1
            if len(a) > 2*len(B) and B not in a:
                return -1
        return i
            
