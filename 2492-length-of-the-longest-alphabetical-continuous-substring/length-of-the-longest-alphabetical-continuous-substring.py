class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        start_index, max_length = 0, 1
        ord_iter = enumerate(map(ord, s))
        _, prev_ord_c = next(ord_iter)
        for i, ord_c in ord_iter:
            if ord_c - prev_ord_c == 1:
                if (local_max_length := (i - start_index) + 1) > max_length:
                    max_length = local_max_length
            else:
                start_index = i
            prev_ord_c = ord_c
                
        return max_length