class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for row in box:
            i, j = len(row) - 2, len(row) - 1
            while i >= 0:
                if row[j] == '.':
                    if row[i] == '#':
                        # swap
                        row[j] = '#'
                        row[i] = '.'
                        j-=1
                        i-=1
                    elif row[i] == '.':
                        i-=1
                    elif row[i] == '*':
                        j = i-1
                        i = j-1
                else:
                    j-=1
                    i=j-1
        # take the transpose of the matrix
        new_box = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                new_box[j][m-1-i] = box[i][j]
        return new_box