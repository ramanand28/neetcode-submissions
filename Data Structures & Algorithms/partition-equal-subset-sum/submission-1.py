class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        memo = {}

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False

            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i, target)] = (
                dfs(i + 1, target) or
                dfs(i + 1, target - nums[i])
            )

            return memo[(i, target)]

        return dfs(0, target)
        