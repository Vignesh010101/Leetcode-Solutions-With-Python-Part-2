class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        idx = defaultdict(list)
        for i, num in enumerate(nums):
            idx[num].append(i)
        idx = dict(sorted(idx.items()))
        
        res = [0] * len(queries)
        for i, (s, t) in enumerate(queries):
            prev = 0
            min_diff = inf
            for num, idx_list in idx.items():
                ns = bisect_left(idx_list, s)
                nt = bisect_right(idx_list, t, lo=ns)
                if ns < nt <= len(idx_list):
                    if prev: 
                        min_diff = min(min_diff, num-prev)
                        if min_diff == 1:
                            break
                    prev = num
            res[i] = min_diff if min_diff != inf else -1
        return res
        