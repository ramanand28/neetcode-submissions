import heapq
import sys
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Build adjacency list
        # adj[u] contains (neighbor, weight)
        adj = [[] for _ in range(n + 1)]

        for u, v, w in times:
            adj[u].append((v, w))

        # Min-heap storing pairs of (distance, node)
        pq = []

        # Nodes are numbered from 1 to n
        dist = [sys.maxsize] * (n + 1)

        # Distance from source k to itself is 0
        dist[k] = 0
        heapq.heappush(pq, (0, k))

        # Process all reachable nodes
        while pq:
            d, u = heapq.heappop(pq)

            # If this is an outdated distance, skip it
            if d > dist[u]:
                continue

            # Explore all neighbors of u
            for v, w in adj[u]:

                # If going through u gives a shorter path to v
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        # Find the maximum shortest-path distance
        # because the signal must reach every node
        max_time = max(dist[1:])

        # If any node is unreachable, return -1
        if max_time == sys.maxsize:
            return -1

        return max_time