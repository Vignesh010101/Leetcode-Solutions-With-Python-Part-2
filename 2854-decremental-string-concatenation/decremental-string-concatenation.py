class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        starts = [word[0] for word in words]
        ends = [word[-1] for word in words]
        
        @cache
        def max_rm(i, s, e):
            if i == len(words): return 0
            return max(
                (1 if e == starts[i] else 0) + max_rm(i + 1, s, ends[i]),
                (1 if s == ends[i] else 0) + max_rm(i + 1, starts[i], e)
            )
        
        return sum(len(word) for word in words) - max_rm(1, starts[0], ends[0])