class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def check(left, right, memo):
            if left > right:
                return 0
            if left == right:
                return nums[left]
            if not (left, right) in memo:
                ss = sum(nums[left: right + 1])
                l, r = ss - check(left + 1, right, memo) + nums[left], ss - check(left, right - 1, memo) + nums[right]
                memo[(left, right)] = max(l, r)
            return memo[(left, right)]

        s = sum(nums)
        c1 = check(0, len(nums) - 1, {})
        return c1 >= s - c1
