import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Min heap stores (time, row, col)
        # Start from (0, 0) with its elevation as initial time
        minHeap = [(grid[0][0], 0, 0)]

        # Mark starting cell as visited
        visit = {(0, 0)}

        # Four directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minHeap:
            # Get the cell with minimum required water level
            time, r, c = heapq.heappop(minHeap)

            # If destination is reached, return minimum time
            if r == n - 1 and c == n - 1:
                return time

            # Explore all four adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries and avoid visited cells
                if (0 <= nr < n and
                    0 <= nc < n and
                    (nr, nc) not in visit):

                    # Mark cell visited when adding to heap
                    visit.add((nr, nc))

                    # Water level must be at least the maximum
                    # elevation encountered along the path
                    newTime = max(time, grid[nr][nc])

                    # Add neighboring cell to min heap
                    heapq.heappush(minHeap, (newTime, nr, nc))