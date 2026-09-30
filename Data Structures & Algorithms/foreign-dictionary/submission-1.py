from collections import deque

class Solution:
    def foreignDictionary(self, words):

        # Create a graph node for every unique character
        # adj[char] stores all characters that must come after char
        adj = {c: set() for word in words for c in word}

        # indegree[char] = number of characters that must come before char
        indegree = {c: 0 for c in adj}

        # Compare every pair of adjacent words
        for i in range(len(words) - 1):

            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))

            # Invalid prefix case
            # Example: ["abc", "ab"]
            # Longer word cannot appear before its exact prefix
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Find the first position where the two words differ
            for j in range(minLen):

                if w1[j] != w2[j]:

                    # Since w1 appears before w2,
                    # w1[j] must come before w2[j]
                    #
                    # Example:
                    # "wrt"
                    # "wrf"
                    #
                    # t comes before f
                    # so create edge: t -> f

                    # Only add the edge if it does not already exist
                    # This prevents increasing indegree twice
                    if w2[j] not in adj[w1[j]]:

                        adj[w1[j]].add(w2[j])

                        # w2[j] now has one more prerequisite
                        indegree[w2[j]] += 1

                    # Only the first different character matters
                    break

        # Add all characters with indegree 0 to the queue
        # These characters have nothing that must come before them
        q = deque()

        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        # Store the final topological order
        res = []

        # Kahn's Algorithm / BFS Topological Sort
        while q:

            # Take a character that currently has no prerequisites
            char = q.popleft()

            # Add it to the result
            res.append(char)

            # Visit all characters that come after this character
            for neighbor in adj[char]:

                # We have now processed one prerequisite
                indegree[neighbor] -= 1

                # If all prerequisites are processed,
                # this character can now be added to the queue
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # If we could not process every character,
        # there must be a cycle
        #
        # Example:
        # a -> b -> c -> a
        if len(res) != len(indegree):
            return ""

        # Convert list of characters into a string
        return "".join(res)