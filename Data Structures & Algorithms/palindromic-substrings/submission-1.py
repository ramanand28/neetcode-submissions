class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        dp = [[None] * n for _ in range(n)]

        def dfs(i, j):
            # Base case: single character or empty substring
            if i >= j:
                return True

            # Return cached result
            if dp[i][j] is not None:
                return dp[i][j]

            # Check whether substring is palindrome
            if s[i] == s[j] and (j - i <= 2 or dfs(i + 1, j - 1)):
                dp[i][j] = True
            else:
                dp[i][j] = False

            return dp[i][j]

        # Check all possible substrings
        for i in range(n):
            for j in range(i, n):
                if dfs(i, j):
                    count += 1

        return count