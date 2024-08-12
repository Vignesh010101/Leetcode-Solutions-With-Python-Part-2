class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        d={}
        for x in range(97,123):
            d[chr(x)]=0
        d["a"]=1
        d["e"]=1
        d["i"]=1
        d["o"]=1
        d['u']=1
        le=len(words)
        l=[0]*len(words)
        y=0
        for x in words:
            if d[x[0]]==1 and d[x[-1]]==1:
                l[y]=1
            y+=1
        p_sum=[0]*len(words)
        prefix=0
        for x in range(len(l)):
            prefix+=l[x]
            p_sum[x]=prefix
        print(p_sum)
        l=[]
        for x in range(0,len(queries)):
            c=queries[x][1]
            d=queries[x][0]
            if queries[x][0]==0:
                l.append(p_sum[c])
            else:
                l.append(p_sum[c]-p_sum[d-1])
        return l

        


            
                

            
                