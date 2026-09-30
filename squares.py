class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        if rows < 3 or cols < 3:
            return 0
        
        def is_magic(r, c):
            nums = set()
            
   
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] < 1 or grid[i][j] > 9:
                        return False
                    nums.add(grid[i][j])
            
            if len(nums) != 9:
                return False
            
            s = sum(grid[r][c:c+3])
            
            for i in range(r, r + 3):
                if sum(grid[i][c:c+3]) != s:
                    return False
            
            
            for j in range(c, c + 3):
                if grid[r][j] + grid[r+1][j] + grid[r+2][j] != s:
                    return False
            
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False
            
            return True
        
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic(i, j):
                    count += 1
        
        return count
