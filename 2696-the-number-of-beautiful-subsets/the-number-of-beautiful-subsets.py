class Solution:
    def solve(self, index, nums, map, k):
        if index == len(nums):
            if len(map) != 0:
                return 1
            return 0
        
        include = 0
        
        if (nums[index] + k) not in map and (nums[index] - k) not in map:
            map[nums[index]] = map.get(nums[index], 0) + 1
            include = self.solve(index + 1, nums, map, k)
            map[nums[index]] -= 1
            if map[nums[index]] == 0:
                del map[nums[index]]
        
        exclude = self.solve(index + 1, nums, map, k)
        
        return include + exclude
    
    def beautifulSubsets(self, nums, k):
        return self.solve(0, nums, {}, k)