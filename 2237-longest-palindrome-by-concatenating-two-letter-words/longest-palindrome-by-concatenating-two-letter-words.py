class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts  = Counter(words)
        has_double = False
        for word in counts.keys():
            if word != word[::-1]:
                counts[word] = min(counts[word], counts[word[::-1]])
            else:
                if counts[word] % 2:
                    has_double = True
                counts[word] = counts[word] - (counts[word] % 2)
        return 2*(sum(counts.values())+int(has_double))