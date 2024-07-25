class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d={}
        for i in knowledge:
            d[i[0]]=i[1]
        temp=''
        res=''
        flag=0
        for i in s:
            if i=='(':
                flag=1
            elif i!=')' and flag==1:
                temp=temp+i
            elif i==')':
                if temp in d.keys():
                    res=res+d[temp]
                else:
                    res=res+'?'
                temp=''
                flag=0
            else:
                res=res+i
        return res