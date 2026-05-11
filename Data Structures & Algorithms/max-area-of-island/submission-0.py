class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        max_area = 0

        def bfs(sr, sc):
            
            grid[sr][sc] = 0
            queue = deque()
            queue.append((sr, sc))
            area = 0
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr , nc = dr + r, dc + c
                    if (0 <= nr < ROWS and 0 <= nc < COLUMNS and grid[nr][nc] == 1):
                        queue.append([nr, nc])
                        grid[nr][nc] = 0
                area += 1
                
            return area
            


        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == 1:
                    max_area = max(max_area, bfs(row, col))
        
        return max_area