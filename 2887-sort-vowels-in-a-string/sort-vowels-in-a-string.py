class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        collected = sorted([char for char in s if char in vowels])
        string = ""
        i = 0
        for char in s:
            if char in vowels:
                string += collected[i]
                i += 1
            else:
                string += char
        return string