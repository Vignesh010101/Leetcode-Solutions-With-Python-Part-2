class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums=[1]
        v2=0
        v3=0
        v5=0

        while len(nums)<n:
            nxt2=nums[v2]*2
            nxt3=nums[v3]*3
            nxt5=nums[v5]*5
            nxt=min(nxt2,nxt3,nxt5)
            if nxt==nxt2:
                v2+=1
            if nxt==nxt3:
                v3+=1
            if nxt==nxt5:
                v5+=1
            nums.append(nxt)

        return nums[-1]