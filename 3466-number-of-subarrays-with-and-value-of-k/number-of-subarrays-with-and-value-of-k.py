class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        s=Counter()
        res=0
        for n in nums:
            ns=Counter()
            for ss,v in s.items():
                ns[ss & n]+=v
            ns[n]+=1
            res+=ns[k]
            s=ns
        return res