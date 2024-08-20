class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        ans = 0 
        rowchng, colchng = 0,0
        row, col = set(), set()
        for i in range(len(queries)-1,-1,-1):
            typ, ind, val = queries[i]
            if typ == 0:
                if ind not in row:
                    row.add(ind)
                    ans += (n-colchng)*val
                    rowchng += 1
            else:
                if ind not in col:
                    ans += (n-rowchng)*val
                    colchng += 1
                    col.add(ind)
        return ans