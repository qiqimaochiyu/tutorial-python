class Solution:
    """
    @param: nums : A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        max = nums[0]
        this_max = 0
        for i in nums:
            this_max += i
            if this_max > max:
                max = this_max
            if this_max < 0:
                this_max = 0
        return max
    
