class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        m, n = Counter(s), Counter(t)
        return m==n
    
    
def isAnagram1(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2
    
def isAnagram2(self, s, t):
    dic1, dic2 = [0]*26, [0]*26
    for item in s:
        dic1[ord(item)-ord('a')] += 1
    for item in t:
        dic2[ord(item)-ord('a')] += 1
    return dic1 == dic2
    
def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)