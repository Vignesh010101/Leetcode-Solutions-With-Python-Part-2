class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        res = []
        for i in range(max_len):
            vert_words = ''
            for word in words:
                if i < len(word):
                    vert_words += word[i]
                else:
                    vert_words += ' '
            res.append(vert_words.rstrip())
        return res