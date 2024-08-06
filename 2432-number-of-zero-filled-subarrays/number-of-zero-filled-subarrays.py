class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        num_subarr = 0
        nums.append(-1)
        for num in nums:
            if num == 0:
                count += 1
            elif count > 0:
                num_subarr += (count + 1) * count // 2
                count = 0

        return num_subarr    