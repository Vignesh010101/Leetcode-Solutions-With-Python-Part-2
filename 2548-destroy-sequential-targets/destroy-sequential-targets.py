class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        buf = nums.copy()
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] % space

        t = Counter(nums).most_common(1)[0][0]
        idx = nums.index(t)
        return buf[idx]