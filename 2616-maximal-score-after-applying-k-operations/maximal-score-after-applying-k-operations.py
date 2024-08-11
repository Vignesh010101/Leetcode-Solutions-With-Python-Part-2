class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        nums, ans = [-n for n in nums], 0
        heapify(nums)

        n = heappop(nums)
        for _ in range(k):
            ans-= n
            n = heappushpop(nums, floor(n/3))

        return ans