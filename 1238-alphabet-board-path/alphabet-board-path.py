class Solution:
    MAPPING = {
        ltr: (i // 5, i % 5)
        for i, ltr in enumerate(ascii_lowercase)
    }

    def alphabetBoardPath(self, target: str) -> str:
        x, y = 0, 0
        path = ''

        for c in target:
            n_x, n_y = self.MAPPING[c]

            if n_y < y:
                path += 'L' * (y - n_y)
            if n_x < x:
                path += 'U' * (x - n_x)
            if n_x > x:
                path += 'D' * (n_x - x)
            if n_y > y:
                path += 'R' * (n_y - y)

            path += '!'
            x, y = n_x, n_y

        return path