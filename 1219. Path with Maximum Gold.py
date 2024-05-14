class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
                return 0
            visited[i][j] = True
            gold = grid[i][j]
            max_gold = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                max_gold = max(max_gold, dfs(i + dx, j + dy))
            visited[i][j] = False
            return gold + max_gold
        m, n = len(grid), len(grid[0])
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited = [[False] * n for _ in range(m)]
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold