import heapq
from typing import List

class Solution:
    def minInterval(
        self,
        intervals: List[List[int]],
        queries: List[int]
    ) -> List[int]:

        # Sort intervals by start
        intervals.sort()

        minHeap = []
        res = {}
        i = 0

        # Process queries in order
        for q in sorted(queries):

            # Add intervals already started
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]

                # Store length and end
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            # Remove expired smallest intervals
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # Save smallest valid length
            res[q] = minHeap[0][0] if minHeap else -1

        # Restore original query order
        return [res[q] for q in queries]