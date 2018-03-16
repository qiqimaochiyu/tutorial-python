class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                res[i] += res[i-1]
        return max(res) if nums else 0
