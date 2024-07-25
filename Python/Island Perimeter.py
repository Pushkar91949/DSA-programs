class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans += 4

                    if r>0 and grid[r-1][c] == 1:
                        ans -= 2
                    if c>0 and grid[r][c-1] == 1:
                        ans -= 2
        return ans
# Question link: https://leetcode.com/problems/island-perimeter/
