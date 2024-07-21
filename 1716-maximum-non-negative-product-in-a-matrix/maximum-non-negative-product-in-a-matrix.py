class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        def isBound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        @lru_cache(None)
        def dfs(row,col,product):
            if not isBound(row, col):
                    return -1
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return product * grid[row][col]
            return max(dfs(row+1,col, product * grid[row][col]),dfs(row,col+1, product * grid[row][col]))           
        max_product = dfs(0,0,1)
        return max_product %(10**9+7) if max_product!=-1 else -1
           