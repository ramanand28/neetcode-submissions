class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def dfs(root):
            nonlocal res

            # Handle empty nodes
            if not root:
                return 0

            # Ignore negative left paths
            left = max(0, dfs(root.left))

            # Ignore negative right paths
            right = max(0, dfs(root.right))

            # Update maximum path sum
            res = max(res, root.val + left + right)

            # Return best downward path
            return root.val + max(left, right)

        dfs(root)
        return res