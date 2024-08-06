import heapq
from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        store=defaultdict(list)
        for n in nums:
            val=n
            rem=0

            while n:
                rem+=n%10
                n=n//10

            store[rem].append(val)

            if len(store[rem])>2:
                heapq.heapify(store[rem])
                heapq.heappop(store[rem])

        res=-1
        for i in store:
            if len(store[i])>1:
                res=max(sum(store[i]),res)

        return res