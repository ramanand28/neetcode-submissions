class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        (nr, nc) in visit or
                        grid[nr][nc] == -1):
                        continue

                    visit.add((nr, nc))
                    q.append((nr, nc))

            dist += 1