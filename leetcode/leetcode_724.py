class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sum(nums)
        m = 0
        for i in range(len(nums)):
            if 2*m + nums[i] == n:
                return i
            m += nums[i]

        return -1
