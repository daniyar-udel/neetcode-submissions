class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        max_area = 0

        def bfs(sr, sc):
            queue = deque()
            queue.append((sr, sc))
            grid[sr][sc] = 0
            area = 0

            while queue:
                r, c = queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLUMNS and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        grid[nr][nc] = 0
                area += 1
            return area

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    max_area = max(max_area, area)
        
        return max_area

        