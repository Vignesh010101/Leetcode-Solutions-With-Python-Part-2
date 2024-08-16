class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods = [0] * value
        for num in nums:
            mods[num % value] += 1

        minv = int(1e6)
        minidx = -1
        for i in range(value):
            if mods[i] < minv:
                minv = mods[i]
                minidx = i

        return minv * value + minidx