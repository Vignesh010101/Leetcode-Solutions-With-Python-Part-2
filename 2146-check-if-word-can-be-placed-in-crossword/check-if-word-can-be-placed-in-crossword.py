class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        k = len(word)

        def get_line(i, j, di, dj):
            pos = 0
            result = []
            while i < m and j < n:
                if pos > k:
                    return [], -1
                value = board[i][j]
                if value == '#':
                    break
                if value != ' ':
                    result.append((pos, value))
                i += di
                j += dj
                pos += 1
            return result, pos
        
        def check_line(positions):
            for pos, char in positions:
                if word[pos] != char:
                    return False
            return True

        def check_reverse_line(positions):
            for pos, char in positions:
                if word[-pos - 1] != char:
                    return False
            return True

        def check(i, j, di, dj):
            chars, length = get_line(i, j, di, dj)
            if length != len(word):
                return False
            if len(chars) == 0:
                return True
            return check_line(chars) or check_reverse_line(chars)

        for i, line in enumerate(board):
            for j, elem in enumerate(line):
                if elem != '#':
                    if j == 0 or line[j - 1] == '#':
                        if check(i, j, 0, 1):
                            return True
                    if i == 0 or board[i - 1][j] == '#':
                        if check(i, j, 1, 0):
                            return True
        return False