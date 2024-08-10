class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        index_k,n = -1, len(nums)
        for i in range(len(nums)):
            if nums[i]==k:
                index_k = i
                break
        d = defaultdict(int)
        current_sum = 0
        for x in range(index_k, n):
            if nums[x]>k:
                current_sum+=1
            elif nums[x]<k:
                current_sum-=1
                
            d[current_sum]+=1
        result, current_sum = 0,0
        for x in range(index_k, -1,-1):
            if nums[x]>k:
                current_sum+=1
            elif nums[x]<k:
                current_sum-=1
            result+= d[-1*current_sum] + d[1-current_sum]
        return result
            