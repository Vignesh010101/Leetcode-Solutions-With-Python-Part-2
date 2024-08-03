class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        visited = [[0] * n for _ in range(m)]
        for i, j in walls:
            visited[i][j] = -1
        for i, j in guards:
            visited[i][j] = -1
        def search(i, j):
            ans = 0
            #up
            r = i - 1
            while r >= 0 and visited[r][j] != -1:
                if visited[r][j] == 0:
                    visited[r][j] = 1
                    ans += 1
                r -= 1
            #down
            r = i + 1
            while r < m and visited[r][j] != -1:
                if visited[r][j] == 0:
                    visited[r][j] = 1
                    ans += 1
                r += 1
            #left
            c = j - 1
            while c >= 0 and visited[i][c] != -1:
                if visited[i][c] == 0:
                    visited[i][c] = 1
                    ans += 1
                c -= 1
            #right
            c = j + 1
            while c < n and visited[i][c] != -1:
                if visited[i][c] == 0:
                    visited[i][c] = 1
                    ans += 1
                c += 1
            return ans
        ans = m*n
        for i, j in guards:
            ans -= search(i, j)
        return ans - len(guards) - len(walls) 
