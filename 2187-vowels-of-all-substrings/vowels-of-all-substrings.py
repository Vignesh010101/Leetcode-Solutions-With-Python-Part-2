class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = 'aeiou'
        total = 0
        for i, char in enumerate(word) :
            if char in vowels :
                total += (i+1) * (n-i) 
        return total