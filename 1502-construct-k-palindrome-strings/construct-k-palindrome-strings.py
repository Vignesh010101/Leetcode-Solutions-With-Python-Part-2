from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        h = Counter(s)
        countOdd = 0
        for value in h.values():
            if value % 2:
                countOdd += 1
        if countOdd > k:
            return False
        return True