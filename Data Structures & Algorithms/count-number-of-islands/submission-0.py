class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        islands = 0

        def bfs(sr, sc):
            
            grid[sr][sc] = '0'
            queue = deque()
            queue.append((sr, sc))
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr , nc = dr + r, dc + c
                    if (0 <= nr < ROWS and 0 <= nc < COLUMNS and grid[nr][nc] == '1'):
                        queue.append([nr, nc])
                        grid[nr][nc] = '0'


        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == '1':
                    bfs(row, col)
                    islands += 1
        
        return islands