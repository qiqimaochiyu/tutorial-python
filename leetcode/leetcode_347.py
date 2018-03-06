class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        res = Counter(nums)
        l = list(res.keys())
        L = l[:k]
        for i in l[k:]:
            L.sort(key=lambda x:-res[x])
            if res[i] > res[L[-1]]:
                L.pop()
                L += [i,]
        return L
        
