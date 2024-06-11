class Solution:
    def minOperations(self, nums: List[int], x: List[int]) -> int:
        commonGcd = x[0]

        for i in range(1, len(x)):
            commonGcd = min(commonGcd, gcd(x[i], commonGcd))

        heapify(nums)
        ans = 0

        while nums:
            num = heappop(nums)

            if commonGcd >= num and commonGcd % num == 0:
                return ans

            ans += 1

        return -1