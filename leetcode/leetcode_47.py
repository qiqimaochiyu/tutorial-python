class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for num in nums:
            ans = [l[:i] + [num] + l[i:] for l in ans for i in range((l+[num]).index(num)+1) ]
        return ans
