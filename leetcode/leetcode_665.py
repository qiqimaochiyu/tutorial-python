class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        a = nums[:]
        b = nums[:]
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                a[i] = nums[i+1]
                b[i+1] = nums[i]
                break
        return a == sorted(a) or b == sorted(b)
