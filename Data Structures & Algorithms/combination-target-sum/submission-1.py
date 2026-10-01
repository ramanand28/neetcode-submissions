from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):

            # Found a valid combination
            if total == target:
                res.append(cur.copy())
                return

            # No more numbers available
            if i >= len(nums):
                return

            # Since nums is sorted, if adding nums[i]
            # already exceeds target, larger numbers will also exceed it
            if total + nums[i] > target:
                return

            # -------------------------
            # Choice 1: Take nums[i]
            # -------------------------
            cur.append(nums[i])

            # Use i again because we can reuse the same number
            dfs(i, cur, total + nums[i])

            # Backtrack
            cur.pop()

            # -------------------------
            # Choice 2: Skip nums[i]
            # and move to the next number
            # -------------------------
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res