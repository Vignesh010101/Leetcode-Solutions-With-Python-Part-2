class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        last = '0'
        for b in target:
            if last != b:
                count += 1
                last = b
        return count