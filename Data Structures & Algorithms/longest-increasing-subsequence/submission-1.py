class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        memo = {}

        def dfs(i, j):
            if i == n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            LIS = dfs(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            memo[(i, j)] = LIS
            return LIS

        return dfs(0, -1)
        