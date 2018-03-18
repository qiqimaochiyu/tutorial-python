class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        m = max(nums)
        L = [0] * (m+1)
        for i in nums:
            L[i] += i
        last, now = 0, 0
        for i in L:
            last, now = now, max(last+i, now)
        return now
