class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        
        left = []
        localmax = 0
        Max = -float('inf')
        for num in nums:
            localmax = max(num, localmax+num)
            Max = max(localmax, Max)
            left.append(Max)
        localmax = 0
        Max = -float('inf')
        res = -float('inf')
        for i in range(1, len(nums))[::-1]:
            localmax = max(nums[i], localmax+nums[i])
            Max = max(localmax, Max)
            res = max(res, left[i-1]+Max)
        return res 
