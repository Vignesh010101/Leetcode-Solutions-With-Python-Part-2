class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        starting_point = 0
        last_repetetive = 0
        current_max = 0
        previous_symb = s[0]
        for i, current_symb in enumerate(s):
            if previous_symb == current_symb:
                if last_repetetive:
                    starting_point = last_repetetive
                last_repetetive = i
            current_max = max(i - starting_point + 1, current_max)
            previous_symb = current_symb
        return current_max


