class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = big = small = nums[0]
        for i in nums[1:]:
            big, small = max(i, i*big, i*small), min(i, i*big, i*small)
            mx = max(mx,  big)
        return mx
