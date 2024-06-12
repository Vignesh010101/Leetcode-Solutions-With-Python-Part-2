class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d = dict()
        for i in words:
            s=""
            for j in range(len(i)):
                s+=i[j]
                if s in d:
                    d[s]+=1
                else:
                    d[s]=1
        l=[]
        for i in words:
            c = 0
            s=""
            for j in range(len(i)):
                s+=i[j]
                c+=d[s]
            l.append(c)
        return l