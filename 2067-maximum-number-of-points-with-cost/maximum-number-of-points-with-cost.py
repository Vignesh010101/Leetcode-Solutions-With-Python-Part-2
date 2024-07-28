class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def goright(row): 
            for i in range(1, len(row)):
                if row[i-1] - 1 > row[i]: 
                    row[i] = row[i-1]-1

        def goleft(row): 
            for i in range(len(row)-2, -1, -1):
                if row[i+1]-1 > row[i]:
                    row[i] = row[i+1]-1

        goright(points[0])
        goleft(points[0])

        res = 0
        for i in range(1, len(points)):
            for j in range(len(points[i])):
                points[i][j] += points[i-1][j]
            goright(points[i])
            goleft(points[i])

        return max(points[-1])