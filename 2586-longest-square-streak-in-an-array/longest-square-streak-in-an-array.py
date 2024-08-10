class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        s = set(nums)
        nums, ans = sorted(s), 0
        s = {n for n in s if n%4 < 2}

        for n in nums:
            square, tally = n*n, 1

            while square in s:
                s.remove(square)
                tally+= 1
                square*= square

            ans = max(ans, tally)
   
        return ans if ans > 1 else -1