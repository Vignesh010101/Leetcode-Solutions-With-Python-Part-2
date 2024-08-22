from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        vals = SortedList()
        ans = inf 
        for i, v in enumerate(nums): 
            if i >= x: 
                vals.add(nums[i-x])
                k = vals.bisect_left(v)
                if k: ans = min(ans, v - vals[k-1])
                if k < len(vals): ans = min(ans, vals[k] - v)
        return ans