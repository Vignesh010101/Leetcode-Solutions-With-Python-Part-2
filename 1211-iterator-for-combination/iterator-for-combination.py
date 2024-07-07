class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        l=[]
        chars=list(characters)
        N=2**len(characters)
        for i in range(N):
            nums=list(str(bin(i)).replace('0b','').zfill(len(chars)))
            if(list(nums).count('1')==combinationLength):
                ans = [int(nums[j]) * chars[j] for j in range(len(chars))]
                final=''.join(ans)
                l.append(final)
        l.sort()
        self.p=l
        self.itr=0
        self.end=len(l)
        

    def next(self) -> str:
        i=self.itr
        x=self.p[i]
        i+=1
        self.itr=i
        return(x)

    def hasNext(self) -> bool:
        return(self.itr<self.end)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()