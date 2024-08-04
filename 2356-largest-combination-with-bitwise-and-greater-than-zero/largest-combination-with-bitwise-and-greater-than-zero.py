class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_elm = max(candidates)

        i = 1
        res = 0
        while i <= max_elm:
            current = 0
            for c in candidates:
                if i & c == i:
                    current += 1
            
            res = max(res, current)

            i = i << 1
        return res