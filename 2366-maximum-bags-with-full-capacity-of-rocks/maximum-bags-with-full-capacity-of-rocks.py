import heapq

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        missing_rocks = []
        num_full_bags = 0
        
        for idx, bag in enumerate(capacity):
            heapq.heappush(missing_rocks, bag - rocks[idx])
        
        while missing_rocks:
            additionalRocks -= heapq.heappop(missing_rocks)
            if additionalRocks >= 0:
                num_full_bags += 1
        
        return num_full_bags