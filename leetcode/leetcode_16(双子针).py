class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = sum(nums[:3])
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                r = nums[i] + nums[j] + nums[k]
                if r == target:
                    return target
                if abs(r - target) < abs(res - target):
                    res = r
                if r > target:
                    k -= 1
                elif r < target:
                    j += 1
        return res
