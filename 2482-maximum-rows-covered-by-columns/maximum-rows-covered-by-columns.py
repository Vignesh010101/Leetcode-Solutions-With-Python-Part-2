class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        res = []
        M = len(mat)
        N = len(mat[0])
        def check(seen):
            count = 0
            for row in mat:
                flag = True
                for c in range(N): 
                    if row[c] == 1:
                        if c in seen:
                            continue
                        else:
                            flag = False
                            break
                if flag:    
                    count +=1   
            res.append(count)
                     
        def solve(c,seen,cols):
            if cols == 0:
                check(seen)
                return
            if c == N:
                return
            else:
                seen.add(c)
                solve(c+1,seen,cols-1)
                seen.remove(c)
                solve(c+1,seen,cols)
        seen = set()
        solve(0,seen,cols)
        return max(res)