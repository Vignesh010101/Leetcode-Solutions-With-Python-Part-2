class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = []
        nums.sort()
        prev = 0
        for num in nums:
            prev += num
            prefix.append(prev)
        
        data = []
        for target in queries:
            i = 0
            k = len(prefix)
            tot = 0
            while i < k:
                j = (i + k) // 2
                if nums[j] > target: k = j
                else: i = j + 1
        
            backs = prefix[i - 1] if i != 0 else 0
            tot += i * target - backs
            tot += (prefix[-1] - backs) - (len(nums) - i) * target
            data.append(tot)
        
        return data