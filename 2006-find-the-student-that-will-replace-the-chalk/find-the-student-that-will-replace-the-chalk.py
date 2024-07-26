from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)
        
        k %= total
        for i in range(n):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        
        return -1 