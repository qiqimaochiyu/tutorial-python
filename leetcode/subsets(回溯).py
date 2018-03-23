class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        res = [[]]
        nums.sort()
        while nums:
            a = nums.pop(0)
            res += [p+[a] for p in res]
        return res
