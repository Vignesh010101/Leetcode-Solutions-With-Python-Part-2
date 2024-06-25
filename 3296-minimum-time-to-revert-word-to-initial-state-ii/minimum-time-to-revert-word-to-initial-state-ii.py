class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        lps = [0] * len(word)
        i = 1
        length = 0

        while i < len(word):
            if word[i] == word[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        border = lps[-1]
        while border:
            if (len(word) - border) % k == 0:
                return (len(word) - border) // k
            border = lps[border-1]


        # print(lps)
        return (len(word) - 1) // k + 1