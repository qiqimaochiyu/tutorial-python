class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p, q = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                p = q + 1
            if nums[i] < nums[i-1]:
                q = p + 1
        return min(max(p, q), len(nums))
