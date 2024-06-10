class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s_streaks = get_streaks(s)
        
        def check(word: str):
            word_streaks = get_streaks(word)
            if len(s_streaks) != len(word_streaks):
                return False
            for (s_letter, s_streak_len), (word_letter, word_streak_len) in zip(s_streaks, word_streaks):
                if s_letter != word_letter:
                    return False
                if word_streak_len > s_streak_len:
                    return False
                if word_streak_len == s_streak_len:
                    continue
                if s_streak_len < 3:
                    return False
            return True
        return sum(check(word) for word in words)

def get_streaks(word: str):
    streak_letter = word[0]
    streak_len = 0
    res = []
    for letter in word:
        if letter == streak_letter:
            streak_len += 1
        else:
            res.append((streak_letter, streak_len))
            streak_letter = letter
            streak_len = 1
    
    res.append((streak_letter, streak_len))
    return res