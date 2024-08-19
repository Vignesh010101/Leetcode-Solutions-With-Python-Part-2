class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        nums.sort()
        neg_idx=0
        neg_group=1
        for i in range(len(nums)):
            if nums[i]<0:
                neg_group*=nums[i]
                neg_idx+=1
            else:
                break
        if neg_idx<=1:
            neg_group=0
        if neg_idx%2!=0:
            neg_group=neg_group//nums[neg_idx-1]
        pos_group=0
        while i<len(nums):
            if nums[i]>0 and pos_group==0:
                pos_group=nums[i]
            elif nums[i]>0:
                pos_group*=nums[i]
            i+=1
        if min(neg_group,pos_group)==0:
            return max(neg_group,pos_group)
        else:
            return neg_group*pos_group