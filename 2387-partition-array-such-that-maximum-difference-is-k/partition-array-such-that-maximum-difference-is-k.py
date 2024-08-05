class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        count = 0
        if k == 0:
            new = len(set(nums))
            return new
        while right >= 0 and left <= right:
            first, second = nums[left], nums[right]
            if left == right:
                count += 1
                right -= 1
                left = 0
                continue
            if second - first <= k:
                count += 1
                left, right = 0, left - 1
            else: left += 1
        return count