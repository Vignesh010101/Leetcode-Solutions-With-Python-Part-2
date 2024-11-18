class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        numRows, numCols, ans = len(board), len(board[0]), -inf
        horizontal = [[[-inf, -inf] for _ in range(numCols)] for _ in range(numRows)]
        vertical = [[[-inf, -inf] for _ in range(numCols)] for _ in range(numRows)]
        for row in range(numRows):
            for col in range(numCols):
                vertical[row][col][0] = max(board[row][col], vertical[row - 1][col][0] if row else -inf)
                horizontal[row][col][0] = max(board[row][col], horizontal[row][col - 1][0] if col else -inf)
                otherRow, otherCol = numRows - 1 - row, numCols - 1 - col
                vertical[otherRow][otherCol][1] = max(board[otherRow][otherCol], vertical[otherRow + 1][otherCol][1] if row else -inf)
                horizontal[otherRow][otherCol][1] = max(board[otherRow][otherCol], horizontal[otherRow][otherCol + 1][1] if col else -inf)
        topLeft = [[[-inf, -inf]] * numCols for _ in range(numRows)]
        topRight = [[[-inf, -inf]] * numCols for _ in range(numRows)]
        bottomLeft = [[[-inf, -inf]] * numCols for _ in range(numRows)]
        bottomRight = [[[-inf, -inf]] * numCols for _ in range(numRows)]
        for row in range(numRows):
            for col in range(numCols):
                top1, top2 = topLeft[row - 1][col] if row else [-inf, -inf]
                left1, left2 = topLeft[row][col - 1] if col else [-inf, -inf]
                diag1 = topLeft[row - 1][col - 1][0] if row and col else -inf
                first = max(board[row][col], top1, left1)
                second = max(vertical[row - 1][col][0] + horizontal[row][col - 1][0], board[row][col] + diag1, top2, left2) if row and col else -inf
                topLeft[row][col] = [first, second]
        for row in range(numRows):
            for col in range(numCols - 1, -1, -1):
                top1, top2 = topRight[row - 1][col] if row else [-inf, -inf]
                right1, right2 = topRight[row][col + 1] if col < numCols - 1 else [-inf, -inf]
                diag1 = topRight[row - 1][col + 1][0] if row and col < numCols - 1 else -inf
                first = max(board[row][col], top1, right1)
                second = max(vertical[row - 1][col][0] + horizontal[row][col + 1][1], board[row][col] + diag1, top2, right2) if row and col < numCols - 1 else -inf
                topRight[row][col] = [first, second]
        for row in range(numRows - 1, -1, -1):
            for col in range(numCols - 1, -1, -1):
                bottom1, bottom2 = bottomRight[row + 1][col] if row < numRows - 1 else [-inf, -inf]
                right1, right2 = bottomRight[row][col + 1] if col < numCols - 1 else [-inf, -inf]
                diag1 = bottomRight[row + 1][col + 1][0] if row < numRows - 1 and col < numCols - 1 else -inf
                first = max(board[row][col], bottom1, right1)
                second = max(vertical[row + 1][col][1] + horizontal[row][col + 1][1], board[row][col] + diag1, bottom2, right2) if row < numRows - 1 and col < numCols - 1 else -inf
                bottomRight[row][col] = [first, second]
        for row in range(numRows - 1, -1, -1):
            for col in range(numCols):
                bottom1, bottom2 = bottomLeft[row + 1][col] if row < numRows - 1 else [-inf, -inf]
                left1, left2 = bottomLeft[row][col - 1] if col else [-inf, -inf]
                diag1 = bottomLeft[row + 1][col - 1][0] if row < numRows - 1 and col else -inf
                first = max(board[row][col], bottom1, left1)
                second = max(vertical[row + 1][col][1] + horizontal[row][col - 1][0], board[row][col] + diag1, bottom2, left2) if row < numRows - 1 and col else -inf
                bottomLeft[row][col] = [first, second]
        for row in range(numRows):
            for col in range(numCols):
                topLeftScore = topLeft[row - 1][col - 1][1] if row and col else -inf
                topRightScore = topRight[row - 1][col + 1][1] if row and col < numCols - 1 else -inf
                bottomLeftScore = bottomLeft[row + 1][col - 1][1] if row < numRows - 1 and col else -inf
                bottomRightScore = bottomRight[row + 1][col + 1][1] if row < numRows - 1 and col < numCols - 1 else -inf
                score = board[row][col] + max(topLeftScore, topRightScore, bottomLeftScore, bottomRightScore)
                ans = max(ans, score)
        return ans