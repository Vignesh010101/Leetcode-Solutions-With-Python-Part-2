class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        masks = []
        for i in range(m): 
            mask = reduce(xor, (1<<j for j in range(n) if mat[i][j]), 0)
            masks.append(mask)
        ans = 0 
        for x in range(1<<n): 
            if x.bit_count() <= cols: 
                ans = max(ans, sum(mask & x == mask for mask in masks))
        return ans 