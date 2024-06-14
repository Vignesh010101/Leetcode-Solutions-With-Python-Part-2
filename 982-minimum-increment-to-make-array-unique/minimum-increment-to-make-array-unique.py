class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        track=0
        minincrement=0

        for num in nums:
            track=max(track,num)
            minincrement+=track-num
            track+=1
        return minincrement