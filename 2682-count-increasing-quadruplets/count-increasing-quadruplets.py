from sortedcontainers import SortedList
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList([nums[0]])
        ans = 0
        for j in range(1, n):
            sl.add(nums[j])
            cnt = 1 if nums[j] < nums[-1] else 0
            for k in range(n - 2, j, -1):
                if nums[j] < nums[k]:
                    cnt += 1
                    continue
                ans += sl.bisect_left(nums[k]) * cnt
        return ans