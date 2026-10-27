class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        memo = {}

        def dfs(root):
            nonlocal res

            # Handle empty nodes
            if not root:
                return 0

            # Return cached result
            if root in memo:
                return memo[root]

            # Calculate left path
            left = max(0, dfs(root.left))

            # Calculate right path
            right = max(0, dfs(root.right))

            # Update maximum path
            res = max(res, root.val + left + right)

            # Cache downward path
            memo[root] = root.val + max(left, right)

            return memo[root]

        dfs(root)
        return res