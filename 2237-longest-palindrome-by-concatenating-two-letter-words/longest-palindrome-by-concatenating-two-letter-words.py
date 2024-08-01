class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        return (lambda counts : 2*(sum(min(counts[word], counts[word[::-1]]) if word != word[::-1] else counts[word] - (counts[word] % 2) for word in counts.keys())+int(any(word == word[::-1] and counts[word] % 2 for word in counts.keys()))))(Counter(words))