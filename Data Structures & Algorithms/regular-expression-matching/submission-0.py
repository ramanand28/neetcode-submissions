class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # Store previous matching results
        cache = {}

        def dfs(i, j):
            # Pattern completely processed
            if j == n:
                return i == m

            # Return cached result
            if (i, j) in cache:
                return cache[(i, j)]

            # Check current character match
            match = (
                i < m and
                (s[i] == p[j] or p[j] == ".")
            )

            # Check upcoming star
            if j + 1 < n and p[j + 1] == "*":

                # Skip or repeat pattern
                cache[(i, j)] = (
                    dfs(i, j + 2) or
                    (match and dfs(i + 1, j))
                )

                return cache[(i, j)]

            # Match without star
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # Characters cannot match
            cache[(i, j)] = False
            return False

        # Start matching both strings
        return dfs(0, 0)