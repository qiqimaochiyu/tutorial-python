class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(nums, t, index, path, res):
            if t < 0:return
            if t == 0:res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, t-nums[i], i, path+[nums[i]], res)
        res = []
        dfs(candidates, target, 0, [], res)
        return res
