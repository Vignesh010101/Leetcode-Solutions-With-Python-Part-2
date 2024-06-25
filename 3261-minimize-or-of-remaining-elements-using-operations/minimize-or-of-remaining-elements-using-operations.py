class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for bit in range(30, -1, -1):
            count, cur, target = 0, (1 << 30) - 1, (ans | ((1 << bit) - 1))
            for num in nums:
                cur &= num
                if cur | target == target:
                    count += 1
                    cur = (1 << 30) - 1
            if len(nums) - count > k: ans |= (1 << bit)
        return ans