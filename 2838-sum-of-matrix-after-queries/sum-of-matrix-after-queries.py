class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        seen_cols = set()
        seen_rows = set() 
        result = 0
        for query in queries[::-1]:
            typ, index, val = query[:]
            if typ and index not in seen_rows:
                result+=(val*n) - (len(seen_cols) * val)
                seen_rows.add(index)
            elif not typ and index not in seen_cols:   
                result+=(val*n) - (len(seen_rows)*val)
                seen_cols.add(index)
        return result
