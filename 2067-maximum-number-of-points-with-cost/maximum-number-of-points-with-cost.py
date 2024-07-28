class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        prev = points[0]
        for i in range(1, n):
            maxer = None
            new = [0]*m
            for j in range(m):
                if not maxer or maxer <= prev[j]:
                    maxer = prev[j]
                new[j] = maxer+points[i][j]
                maxer -= 1
            maxer = None
            for j in range(m-1,-1,-1):
                if not maxer or maxer <= prev[j]:
                    maxer = prev[j]
                new[j] = max(new[j],maxer+points[i][j])
                maxer -= 1
            # print(prev, new)
            prev = list(new)
        return max(prev)