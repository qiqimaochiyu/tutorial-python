class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        """
        
        if len(nums) < 3:
            return False
        stack = [[nums[0], nums[0]]]
        m = nums[0]
        for num in nums[1:]:
            if num <= m:
                m = num
            else:
                while stack and num > stack[-1][0]:
                    if num < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
                stack.append([m, num])
        return False
