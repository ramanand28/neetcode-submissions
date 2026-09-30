from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # Create a graph node for every unique character
        # Using set() avoids duplicate edges
        adj = {c: set() for word in words for c in word}

        # Compare each pair of adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))

            # Invalid case:
            # Example: ["abc", "ab"]
            # A longer word cannot come before its exact prefix
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Find the first different character
            for j in range(minLen):
                if w1[j] != w2[j]:

                    # Since w1 comes before w2,
                    # w1[j] must come before w2[j]
                    adj[w1[j]].add(w2[j])

                    # Only the first different character matters
                    break

        # visited states:
        # character not in visited -> not visited yet
        # visited[char] = True     -> currently in DFS path
        # visited[char] = False    -> completely processed
        visited = {}

        # Stores characters in reverse topological order
        res = []

        def dfs(char):

            # If we have already seen this character
            if char in visited:

                # True means it is currently in DFS path,
                # so we found a cycle
                #
                # False means it was already fully processed
                return visited[char]

            # Mark character as currently being visited
            visited[char] = True

            # Visit all characters that must come after this character
            for nei in adj[char]:

                # If neighbor DFS finds a cycle,
                # propagate True upward
                if dfs(nei):
                    return True

            # Finished exploring this character
            # Remove it from the current DFS path
            visited[char] = False

            # Add after exploring neighbors
            # This gives reverse topological order
            res.append(char)

            # No cycle found
            return False

        # Run DFS from every character
        # because the graph may have disconnected components
        for char in adj:

            # If a cycle exists, no valid ordering is possible
            if dfs(char):
                return ""

        # DFS adds nodes in reverse topological order
        res.reverse()

        # Convert list of characters into the final string
        return "".join(res)