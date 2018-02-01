class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = nums[:]
        for num in nums:
            index = num - 1
            L[index] -= nums[index]
        return [i+1 for i, num in enumerate(L) if num < 0]
