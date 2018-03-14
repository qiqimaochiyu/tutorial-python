class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key

        def cmp(x,y):
            x, y = str(x), str(y)
            if y+x > x+y:
                return 1
            if x+y==y+x:
                return 0
            else:
                return -1
        nums = [str(i) for i in nums]
        nums.sort(key=cmp_to_key(cmp))
        return '0' if nums[0]=='0' else "".join(nums) 
