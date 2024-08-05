class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sc={}
        mxw=0
        ans=''
        for s,m in zip(senders,messages):
            sc[s]=sc.get(s,0)+m.count(' ')+1
            if sc[s]>mxw or (sc[s]==mxw and s>ans): 
                ans=s
                mxw=sc[s]
        return ans

        