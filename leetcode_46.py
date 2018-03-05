class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        return [p[:i] + [nums[0]] + p[i:]
               for p in self.permute(nums[1:])
               for i in range(len(nums))]
        
