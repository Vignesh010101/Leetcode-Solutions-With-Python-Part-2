from heapq import *

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target_sum = sum(nums) / 2
        curr_sum = sum(nums)
        # create maximum heap
        heap = [-num for num in nums]
        heapify(heap)
        
        ans = 0
        while curr_sum > target_sum:
            maxi = abs(heappop(heap)) # get max element
            curr_sum -= maxi / 2
            heappush(heap, -(maxi / 2)) # push halve
            ans += 1
        
        return ans
            


