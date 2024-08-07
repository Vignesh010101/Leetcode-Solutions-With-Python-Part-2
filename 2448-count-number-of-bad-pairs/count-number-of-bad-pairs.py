class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        data= {}
        total = 0
        n = len(nums)
        for i in range(n):
            if nums[i] - i not in data:
                data[nums[i]-i] =1
            else:
                data[nums[i]-i] +=1
        for key in data:
            if data[key]>1:
                total +=(data[key]*(data[key]-1))//2
        return ((n*(n-1)//2)-total)
        