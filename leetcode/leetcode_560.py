class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}
        res, s = 0, 0
        for i in range(len(nums)):
            s += nums[i]
            res += d.get(s-k, 0)
            d[s] = d.get(s, 0) + 1
        return res
