class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(' ')
        m = list(zip(pattern, s))
        return len(set(s))==len(set(m))==len(set(pattern)) and len(pattern)==len(s)
    
    def wordPattern2(self, pattern, str):
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)
