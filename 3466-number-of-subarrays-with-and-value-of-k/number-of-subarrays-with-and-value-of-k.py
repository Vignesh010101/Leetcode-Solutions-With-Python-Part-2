from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_and_counts = defaultdict(int)
        total_count = 0
        
        for num in nums:
            current_and_counts = defaultdict(int)
            
            for prefix_and, count in prefix_and_counts.items():
                and_result = prefix_and & num
                current_and_counts[and_result] += prefix_and_counts[prefix_and]
            
            current_and_counts[num] += 1
            
            for result, count in current_and_counts.items():
                if result == k:
                    total_count += count
            
            prefix_and_counts = current_and_counts
        
        return total_count