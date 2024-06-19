class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        D=[]
        for i in pattern:
            D.append(pattern.count(i))
        L=[]
        for i in (words):
            I=[i.count(j) for j in i]    
            if I==D and [*map(i.index,i)]==[*map(pattern.index,pattern)]:
                L.append(i)
        return L