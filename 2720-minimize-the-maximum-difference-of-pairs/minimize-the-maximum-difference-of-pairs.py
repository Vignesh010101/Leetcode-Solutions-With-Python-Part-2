class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[n - 1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            j, i = 0, 1
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    j += 1
                    i += 1
                i += 1
            if j >= p:
                right = mid
            else:
                left = mid + 1
        return left