class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        i = 0
        j = n-1
        # left strictly increasing array starts from 0
        while i<n-1 and nums[i] < nums[i+1]:
            i += 1
        # right strictly increasing array that ends in n-1
        while 0<j and nums[j-1] < nums[j]:
            j -= 1
        # if nums is strictly increasing, return all subarrays
        if j<=i:
            return (n+1)*n//2
        # for diminishing left array (from index 0), find insert idx in right array
        # every number starts from the insert idx represents a solution: [0...i, k...n-1]
        # including the right empty array, [0...i, ]
        while i >= 0:
            curr = nums[i]
            k = bisect.bisect(nums, curr, lo=j)
            res += (n-k+1)
            i -= 1
        # when left array becomes empty, each number in right array also represents a solution
        # [, j...n-1] including [,], the empty left and empty right
        res += (n-j+1)  
        return res

            
     
    
        
            
            