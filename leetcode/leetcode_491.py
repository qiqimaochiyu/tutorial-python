class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = {()}
        for num in nums:
            subs |= {sub + (num, ) for sub in subs if not sub or sub[-1]<=num}
        return [i for i in subs if len(i)>=2]
